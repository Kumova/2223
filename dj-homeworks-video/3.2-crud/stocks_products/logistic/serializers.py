
from rest_framework import serializers
from logistic.models import StockProduct


class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=60)
    description = serializers.CharField()


class ProductPositionSerializer(serializers.ModelSerializer):
    positions=serializers.CharField()
    price=serializers.DecimalField(max_digits=18, decimal_places=2)
    quantity=serializers.IntegerField()


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        for position in positions:
            StockProduct.objects.create(stock=stock, **position)
        return stock

    def update(self, instance, validated_data):
        stock = super().update(instance, validated_data)
        positions = validated_data.pop('positions')
        for position in positions:
            StockProduct.objects.update_or_create(stock=position['address'], product=position['product'],
                                                  defaults={"quantity": position['quantity'],
                                                            "price": position['price']})

        return stock
