
from rest_framework import serializers
from stocks_products.logistic.models import StockProduct


class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=60)
    description = serializers.CharField()


class ProductPositionSerializer(serializers.ModelSerializer):
    positions=serializers.CharField()
    price=serializers.DecimalField()
    quantity=serializers.IntegerField()




class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)
    # настройте сериализатор для склада

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        serializer = StockSerializer(data=positions)
        serializer.is_valid(raise_exception=True)
        # создаем склад по его параметрам
        stock = super().create(validated_data)
        StockProduct.objects.create(data=positions, **positions)
        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        created = StockProduct.objects.update_or_create(positions='positions', defaults=True)
        return stock
