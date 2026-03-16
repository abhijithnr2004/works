from rest_framework import serializers

from .models import Customer, Product, Bill, BillItem

class CustomerSerializer(serializers.ModelSerializer):

    owner = serializers.StringRelatedField(read_only=True)

    class Meta:

        model = Customer

        fields = ['id', 'owner', 'name', 'phone', 'email', 'address', 'created_at']

        read_only_fields = ['created_at']

class ProductSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:

        model = Product

        fields = ['id', 'owner', 'name', 'unit_price', 'description']

class BillItemSerializer(serializers.ModelSerializer):

    line_total = serializers.SerializerMethodField()

    class Meta:
        
        model = BillItem

        fields = ['id', 'product_name', 'quantity', 'unit_price', 'line_total']

    def get_line_total(self, obj):

        return obj.line_total
    
class BillItemWriteSerializer(serializers.ModelSerializer):
    """
    Write serializer for BillItem — used only when creating items.
    No computed fields needed; just validate the input fields.
    """
    class Meta:

        model = BillItem

        fields = ['product_name', 'quantity', 'unit_price']

class BillReadSerializer(serializers.ModelSerializer):
    """
    Rich read representation for GET requests.
    Nests full customer info and all line items with totals.
    """
    customer = CustomerSerializer(read_only=True)

    items = BillItemSerializer(many=True, read_only=True)

    total_amount = serializers.SerializerMethodField()

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:

        model = Bill

        fields = [
            'id', 'owner', 'bill_number', 'customer',
            'status', 'notes', 'items', 'total_amount', 'created_at'
        ]

    def get_total_amount(self, obj):

        return str(obj.total_amount)
    
class BillWriteSerializer(serializers.ModelSerializer):

    """
    Write serializer for POST requests.
    Accepts a list of items to create alongside the bill.
    Uses nested write to create BillItems in one API call.
    """
    items = BillItemWriteSerializer(many=True)

    class Meta:

        model = Bill

        fields = ['customer', 'bill_number', 'status', 'notes', 'items']

    def validate_items(self, value):

        """
        Custom field-level validation.
        DRF calls validate_<fieldname>() automatically.
        """
        if not value:

            raise serializers.ValidationError(
                "A bill must contain at least one item."
            )
        
        return value
    
    def validate(self, data):
        """
        Cross-field validation — called after individual field validation.
        Here we ensure the customer belongs to the request user.
        """
        request = self.context.get('request')

        customer = data.get('customer')

        if customer and customer.owner != request.user:

            raise serializers.ValidationError(
                {"customer": "You can only bill your own customers."}
            )
        
        return data
    
    def create(self, validated_data):

        """
        Override create() to handle nested BillItem creation.
        DRF doesn't create nested objects automatically — we do it manually.
        """

        items_data = validated_data.pop('items')  # Extract items before creating bill

        validated_data['owner'] = self.context['request'].user

        bill = Bill.objects.create(**validated_data)

        # Create each line item linked to this bill
        for item_data in items_data:

            BillItem.objects.create(bill=bill, **item_data)
            
        return bill
