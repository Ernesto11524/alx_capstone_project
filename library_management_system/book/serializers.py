from rest_framework import serializers
from .models import Book, Transaction

# Serializer for the book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

# Serializer for the transaction model
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    # This is the validation method to validate data.
    def validate(self, attrs):
        check = Transaction.objects.filter(user = attrs['user'], book = attrs['book'])
        if check:
            raise serializers.ValidationError("You have already borrowed this book.")
        return attrs
    
    # This method checks if the number of available copies is not zero.
    def create(self, validated_data):
        transaction = super().create(validated_data)

        book = transaction.book
        if book.number_of_copies_available == 0:
            raise serializers.ValidationError("There are no available books")
        return transaction