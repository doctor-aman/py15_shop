from rest_framework import serializers

from order.models import OrderItem, Order


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    positions = OrderItemSerializer(write_only=True, many=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'positions', 'status']


    def create(self, validated_data):
        products = validated_data.pop('positions')
        user = self.context.get('request').user
        order = Order.objects.create(user=user, status='open')
        for prod in products:
            product = prod['product']
            quantity = prod['quantity']
            OrderItem.objects.create(order=order,
                                     product=product,
                                     quantity=quantity)
        return order

    def to_representation(self, instance): # сериализируем для того чтобы показать positions в postman
        representation = super().to_representation(instance)
        representation['positions'] = OrderItemSerializer(instance.items.all(), many=True).data


        return representation
