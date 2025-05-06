from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Teacher, Student, Class
from .serializers import TeacherSerializer, StudentSerializer, ClassSerializer
import stripe
from django.conf import settings
from rest_framework.views import APIView
from rest_framework import status

stripe.api_key = settings.STRIPE_SECRET_KEY

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class ChargeClassPaymentView(APIView):
    def post(self, request):
        try:
            # Retrieve data from the request
            class_id = request.data.get('class_id')  # The class the student is paying for
            student_id = request.data.get('student_id')  # The student who is making the payment
            payment_method_id = request.data.get('payment_method_id')  # The payment method ID to be used

            # Fetch the class and student from the database using the provided IDs
            class_obj = Class.objects.get(id=class_id)  # Get the class details from the database
            student = Student.objects.get(id=student_id)  # Get the student details from the database

            # Check if the student has a Stripe customer ID, create one if not
            if not student.stripe_customer_id:
                customer = stripe.Customer.create(
                    email=student.email,  # Create a new Stripe customer for the student
                    name=student.name
                )
                student.stripe_customer_id = customer.id  # Save the Stripe customer ID for future transactions
                student.save()

            # Calculate the total amount in cents (Stripe expects the amount in cents)
            total_amount = int(class_obj.cost * 100)  # Convert the class cost to cents

            # Create the PaymentIntent with Stripe
            payment_intent = stripe.PaymentIntent.create(
                amount=total_amount,  # Total amount to charge the student
                currency=class_obj.currency,  # Currency for the transaction
                customer=student.stripe_customer_id,  # The Stripe customer ID for the student
                payment_method=payment_method_id,  # The payment method ID to charge 
                payment_method_types=['card'],  # Allow card payments only
                confirm=True,  # Confirm the payment immediately
                off_session=True  # Perform the payment off-session
            )

            # After a successful payment, update the student's charged amount in the database
            student.charged_amount += class_obj.cost  # Increment the student's charged amount
            student.save()  # Save the updated student record

            # Respond with success and include the PaymentIntent ID for reference
            return Response({
                "success": True,
                "message": "Payment successful",
                "payment_intent": payment_intent.id  # Return the PaymentIntent ID as confirmation
            })

        except Exception as e:
            return Response({
                "success": False,
                "message": str(e) 
            }, status=status.HTTP_400_BAD_REQUEST)  
