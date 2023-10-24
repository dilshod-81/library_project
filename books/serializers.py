from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','title', 'content','subtitle', 'author', 'isbn', 'price',)

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        # check title if it contains only alphatiacal chars
        if not title.isalpha():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Kitob sarlavhasi harflardan tashkil topgan bo'lsa kerak!"
                }
            )
        # check title and author from database existance
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Kitob sarlavhasi va mualifi bir xil bo'lgan kitobni yuklay olmaysiz!"
                }
            )
        return data
    def validate_price(self, price):
        if price < 0 or price > 9999999999:
            raise ValidationError(
                {
                    "status": False,
                    "message": "Narx noto'g'ri kiritilgan"
                }
            )

# modelda yuq malumotni serializer qilish uchun masalan
# class CashSerializer(serializers.Serializer):
#     input = serializers.CharField(max_length=150)
#     output = serializers.CharField(max_length=120)