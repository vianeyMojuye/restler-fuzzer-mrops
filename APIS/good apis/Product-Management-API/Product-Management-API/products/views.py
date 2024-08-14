from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import  Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
import random
import time

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def retrieve(self, request, *args, **kwargs):
    #     # intentional  bug: Cross data contamination
    #     item_id = int(kwargs.get('pk'))
    #     if item_id % 2 == 0:
    #         # For even IDs, return the product with ID 20 (If It Exists)
    #         try:
    #             product = Product.objects.get(id=20)
    #         except Product.DoesNotExist:
    #             return Response({"error": "Product Not Found"}, status=status.HTTP_404_NOT_FOUND)
    #     else:
    #         product = self.get_object()
    
    #     serializer= self.get_serializer(product)
    #     return  Response(serializer.data)

    # ################ another bug : UPDate cross data contamination
    # def update(self, request, *args, **kwargs):
    #     # Extract the requested item ID
    #     requested_id = int(kwargs.get('pk'))

    #     try:
    #         product = Product.objects.get(id=requested_id)
    #     except Product.DoesNotExist:
    #         return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    
    #     # Intentional bug: Cross-data contamination
    #     if requested_id % 2 == 0:
    #         # For even IDs, mistakenly update item with ID 20 (if it exists)
    #         # update_target_id = 20
    #         product_to_contaminate = Product.objects.get(id=20)
    #         # Apply the same update to product 2
    #         product_to_contaminate.name = request.data.get('name', product_to_contaminate.name)
    #         product_to_contaminate.description = request.data.get('description', product_to_contaminate.description)
    #         product_to_contaminate.price = request.data.get('price', product_to_contaminate.price)
    #         product_to_contaminate.save()

   
    
    #     serializer = self.get_serializer(product, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     ##### Bug :Update an existing product, but introduces a randomness bug.

    def update(self, request, *args, **kwargs):
        """
        Update an existing product, but introduces a randomness bug.
        """
        # Extract the requested item ID
        requested_id = int(kwargs.get('pk'))
        try:
            product = Product.objects.get(id=requested_id)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        # Introduce a delay for POST requests
        time.sleep(5)  # Delays for 5 seconds
        # Introduce randomness: Sometimes update a field with a random value
        if random.choice([True, False]):
            request.data['description'] = f"description-Randomized"
            
        
        serializer = ProductSerializer(product, data=request.data, partial=True)

         
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, *args, **kwargs):
        """
        Delete a product by ID, but introduce a bug that only allows deletion of items with even IDs.
        """
         # Extract the requested item ID
        requested_id = int(kwargs.get('pk'))
        try:
            product = Product.objects.get(id=requested_id)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        # Introduce a delay for POST requests
        time.sleep(5)  # Delays for 5 seconds
        # Introduce the bug: Only delete products with even IDs
        if int(requested_id) % 2 == 0:
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            # If the ID is odd, do not delete and return a 204 No Content response
            return Response(status=status.HTTP_204_NO_CONTENT)


      ##### Bug 3 : POST item1 different than get Item1

    # def create(self, request, *args, **kwargs):
    #     # Serialize the incoming data
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         # Save the new product but introduce a bug by altering the data
    #         product = serializer.save()
    #         # Intentional bug: Modify the product data before saving
    #         product.description = "This is a bugged description"
    #         product.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def retrieve(self, request, *args, **kwargs):
    #     # Retrieve the original product object
    #     product = self.get_object()
    #     serializer = self.get_serializer(product)
    #     data = serializer.data
    #     # Intentional bug: Modify the data before returning
    #     if 'description' in data:
    #         data['description'] = "This is a bugged GET response description"
    #     return Response(data)
    #
    # ##### Bug 4 : Modify the update method to alter the data before saving it.
    #
    # def update(self, request, *args, **kwargs):
    #     # Get the product instance
    #     product = self.get_object()
    #
    #     # Deserialize the incoming data
    #     serializer = self.get_serializer(product, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         # Intentional bug: Modify the data before saving
    #         validated_data = serializer.validated_data
    #         if 'price' in validated_data:
    #             # For demonstration, let's say the price is unintentionally set to 999.99
    #             validated_data['price'] = 999.99
    #
    #         # Save the product with the (possibly altered) validated data
    #         serializer.update(product, validated_data)
    #
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    ###### Bug5 :  POST -> Delete  item1 compare with GET item1 where get item1 returns data instead of data not found message
    # def create(self, request, *args, **kwargs):
    #     # Standard creation logic
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         product = serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def destroy(self, request, *args, **kwargs):
    #     # Intentional bug: Pretend to delete the item but don't actually do it
    #     instance = self.get_object()
    #     # Logically, we should call instance.delete() here, but we'll skip it to simulate a bug
    #     # instance.delete()  # This line is intentionally omitted to introduce the bug
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    #
    # def retrieve(self, request, *args, **kwargs):
    #     # Retrieve the product object
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

    ############ Bug 6 : POST item 1 then PUT item1 compare with POST item2 (was supposed to have same description output) but they don't have
    # def create(self, request, *args, **kwargs):
    #     # Standard creation logic
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         product = serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def update(self, request, *args, **kwargs):
    #     # Get the product instance
    #     product = self.get_object()
        
    #     # Deserialize the incoming data
    #     serializer = self.get_serializer(product, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         # Intentional bug: Alter the product's description during update
    #         validated_data = serializer.validated_data
    #         if 'description' in validated_data:
    #             # Injecting bug: change description to something static
    #             validated_data['description'] = "This description has been altered by a bug"
    #             validated_data['name'] = "This name has been altered by a bug"

    #         # Save the product with the (possibly altered) validated data
    #         serializer.update(product, validated_data)
            
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def retrieve(self, request, *args, **kwargs):
    #     # Retrieve the product object
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)
        

    # ##### Bug 7 : Delete one data affects another
    # def create(self, request, *args, **kwargs):
    #     # Standard creation logic
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         product = serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def destroy(self, request, *args, **kwargs):
    #     # Intentional bug: Deleting one resource affects another
    #     instance = self.get_object()

    #     # Attempt to delete the intended resource (this part is correct)
    #     instance.delete()

    #     # Bug: Also delete another product if it exists, e.g., product with ID 1
    #     # This simulates the incorrect deletion logic where another unrelated product is also deleted
    #     try:
    #         other_product = Product.objects.get(id=1)
    #         other_product.delete()
    #     except Product.DoesNotExist:
    #         # If product with ID 1 does not exist, do nothing
    #         pass

    #     return Response(status=status.HTTP_204_NO_CONTENT)
