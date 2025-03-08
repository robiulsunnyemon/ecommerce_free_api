# E-commerce API Documentation

This repository provides the backend for an e-commerce platform built with Django REST Framework (DRF). Below is the documentation for the available API endpoints.

## Base URL
http://your_ip_address/api/


## Authentication
- This API requires authentication for certain endpoints. Authentication is done using Django's built-in user authentication system.
- Use `IsAuthenticated` or `IsAuthenticatedOrReadOnly` permissions to control access.

## API Endpoints

### 1. **Categories**
- **Endpoint**: `/categories/`
- **Methods**:  
  - `GET`: Retrieve the list of categories  
  - `POST`: Create a new category  
- **Fields**:  
  - `name`: string (required)  
  - `description`: string (optional)  
  - `created_at`: datetime (auto-generated)  
- **Permissions**: `IsAuthenticatedOrReadOnly`

---

### 2. **Products**
- **Endpoint**: `/products/`
- **Methods**:  
  - `GET`: Retrieve the list of products  
  - `POST`: Create a new product  
  - `PUT`: Update an existing product  
  - `DELETE`: Delete a product  
- **Filters**:  
  - `category`: Filter products by category  
  - `price`: Filter products by price  
- **Fields**:  
  - `name`: string (required)  
  - `description`: string (required)  
  - `price`: decimal (required)  
  - `stock`: integer (required)  
  - `category`: foreign key to `Category`  
  - `image`: image (optional)  
  - `created_at`: datetime (auto-generated)  
  - `updated_at`: datetime (auto-generated)  
- **Permissions**: `IsAuthenticatedOrReadOnly`

---

### 3. **Orders**
- **Endpoint**: `/orders/`
- **Methods**:  
  - `GET`: Retrieve a list of orders for the authenticated user  
  - `POST`: Create a new order  
- **Fields**:  
  - `user`: foreign key to `User` (required)  
  - `total_amount`: decimal (required)  
  - `status`: string (choices: 'PENDING', 'PROCESSING', 'SHIPPED', 'DELIVERED', 'CANCELLED')  
  - `created_at`: datetime (auto-generated)  
  - `updated_at`: datetime (auto-generated)  
- **Permissions**: `IsAuthenticated`

---

### 4. **Cart**
- **Endpoint**: `/cart/`
- **Methods**:  
  - `GET`: Retrieve the cart for the authenticated user  
  - `POST`: Create a new cart for the authenticated user  
- **Fields**:  
  - `user`: foreign key to `User` (required)  
  - `items`: list of `CartItem` objects  
  - `created_at`: datetime (auto-generated)  
  - `updated_at`: datetime (auto-generated)  
- **Permissions**: `IsAuthenticated`

---

### 5. **Cart Items**
- **Endpoint**: `/cart-items/`
- **Methods**:  
  - `GET`: Retrieve the list of cart items for the authenticated user  
  - `POST`: Add a new item to the cart  
  - `PUT`: Update the quantity of an item in the cart  
  - `DELETE`: Remove an item from the cart  
- **Fields**:  
  - `cart`: foreign key to `Cart` (required)  
  - `product`: foreign key to `Product` (required)  
  - `quantity`: integer (required)  
- **Permissions**: `IsAuthenticated`

---

### 6. **Reviews**
- **Endpoint**: `/reviews/`
- **Methods**:  
  - `GET`: Retrieve the list of reviews  
  - `POST`: Create a new review for a product  
- **Filters**:  
  - `product`: Filter reviews by product  
  - `rating`: Filter reviews by rating  
- **Fields**:  
  - `product`: foreign key to `Product` (required)  
  - `user`: foreign key to `User` (required)  
  - `rating`: integer (choices: 1-5) (required)  
  - `comment`: text (required)  
  - `created_at`: datetime (auto-generated)  
- **Permissions**: `IsAuthenticatedOrReadOnly`

---

### 7. **User Profile**
- **Endpoint**: `/profile/`
- **Methods**:  
  - `GET`: Retrieve the authenticated user's profile  
  - `POST`: Create or update the user's profile  
- **Fields**:  
  - `user`: foreign key to `User` (required)  
  - `phone`: string (optional)  
  - `address`: text (optional)  
  - `profile_picture`: image (optional)  
- **Permissions**: `IsAuthenticated`

---

### 8. **Wishlist**
- **Endpoint**: `/wishlist/`
- **Methods**:  
  - `GET`: Retrieve the authenticated user's wishlist  
  - `POST`: Add a new product to the user's wishlist  
- **Fields**:  
  - `user`: foreign key to `User` (required)  
  - `products`: many-to-many relation to `Product` (required)  
  - `created_at`: datetime (auto-generated)  
- **Permissions**: `IsAuthenticated`

---

### 9. **Coupons**
- **Endpoint**: `/coupons/`
- **Methods**:  
  - `GET`: Retrieve all available coupons  
  - `POST`: Create a new coupon  
- **Fields**:  
  - `code`: string (unique, required)  
  - `discount_percent`: integer (required)  
  - `valid_from`: datetime (required)  
  - `valid_to`: datetime (required)  
  - `active`: boolean (required)  
- **Permissions**: `IsAuthenticatedOrReadOnly`

---

## Models Overview

### Categories
- **name**: The name of the category.
- **description**: A description of the category.
- **created_at**: The timestamp when the category was created.

### Products
- **name**: The name of the product.
- **description**: The product description.
- **price**: The product price.
- **stock**: The quantity of product available.
- **category**: The category the product belongs to.
- **image**: A product image.
- **created_at**: The timestamp when the product was created.
- **updated_at**: The timestamp when the product was last updated.

### Orders
- **user**: The user who placed the order.
- **total_amount**: The total cost of the order.
- **status**: The status of the order.
- **created_at**: The timestamp when the order was created.
- **updated_at**: The timestamp when the order was last updated.

### Cart
- **user**: The user who owns the cart.
- **items**: The list of items in the cart.
- **created_at**: The timestamp when the cart was created.
- **updated_at**: The timestamp when the cart was last updated.

---

## API Endpoints Table

| Endpoint            | Method  | Description                                     | Request Body                                                                                      | Response                                   | Permissions                |
|---------------------|---------|-------------------------------------------------|---------------------------------------------------------------------------------------------------|-------------------------------------------|----------------------------|
| `/categories/`       | GET     | Retrieve the list of categories                 | None                                                                                              | JSON list of categories                  | `IsAuthenticatedOrReadOnly`|
| `/categories/`       | POST    | Create a new category                           | `{ "name": "string", "description": "string" }`                                                     | Created category object                   | `IsAuthenticated`          |
| `/products/`         | GET     | Retrieve the list of products                   | None                                                                                              | JSON list of products                    | `IsAuthenticatedOrReadOnly`|
| `/products/`         | POST    | Create a new product                            | `{ "name": "string", "description": "string", "price": decimal, "stock": integer, "category": integer, "image": "image_url" }` | Created product object                    | `IsAuthenticated`          |
| `/products/{id}/`    | PUT     | Update an existing product                      | `{ "name": "string", "description": "string", "price": decimal, "stock": integer, "category": integer, "image": "image_url" }` | Updated product object                    | `IsAuthenticated`          |
| `/products/{id}/`    | DELETE  | Delete a product                                | None                                                                                              | Success message                          | `IsAuthenticated`          |
| `/orders/`           | GET     | Retrieve orders for authenticated user          | None                                                                                              | JSON list of orders                      | `IsAuthenticated`          |
| `/orders/`           | POST    | Create a new order                              | `{ "user": integer, "total_amount": decimal, "status": "string" }`                                 | Created order object                     | `IsAuthenticated`          |
| `/cart/`             | GET     | Retrieve the cart for authenticated user        | None                                                                                              | JSON cart object                         | `IsAuthenticated`          |
| `/cart/`             | POST    | Create or update cart for authenticated user    | `{ "user": integer, "items": [{ "product": integer, "quantity": integer }] }`                     | Created or updated cart object           | `IsAuthenticated`          |
| `/cart-items/`       | GET     | Retrieve the cart items for authenticated user  | None                                                                                              | JSON list of cart items                  | `IsAuthenticated`          |
| `/cart-items/`       | POST    | Add a new item to the cart                      | `{ "cart": integer, "product": integer, "quantity": integer }`                                      | Created cart item object                 | `IsAuthenticated`          |
| `/cart-items/{id}/`  | PUT     | Update the quantity of an item in the cart      | `{ "quantity": integer }`                                                                          | Updated cart item object                 | `IsAuthenticated`          |
| `/cart-items/{id}/`  | DELETE  | Remove an item from the cart                    | None                                                                                              | Success message                          | `IsAuthenticated`          |
| `/reviews/`          | GET     | Retrieve reviews                                | None                                                                                              | JSON list of reviews                     | `IsAuthenticatedOrReadOnly`|
| `/reviews/`          | POST    | Create a new review for a product               | `{ "product": integer, "user": integer, "rating": integer, "comment": "string" }`                 | Created review object                    | `IsAuthenticated`          |
| `/profile/`          | GET     | Retrieve the authenticated user's profile       | None                                                                                              | JSON user profile object                 | `IsAuthenticated`          |
| `/profile/`          | POST    | Create or update user's profile                 | `{ "phone": "string", "address": "string", "profile_picture": "image_url" }`                       | Created or updated profile object        | `IsAuthenticated`          |
| `/wishlist/`         | GET     | Retrieve the authenticated user's wishlist      | None                                                                                              | JSON wishlist object                     | `IsAuthenticated`          |
| `/wishlist/`         | POST    | Add a product to the user's wishlist            | `{ "user": integer, "product": integer }`                                                          | Updated wishlist object                  | `IsAuthenticated`          |
| `/coupons/`          | GET     | Retrieve available coupons                      | None                                                                                              | JSON list of coupons                     | `IsAuthenticatedOrReadOnly`|
| `/coupons/`          | POST    | Create a new coupon                             | `{ "code": "string", "discount_percent": integer, "valid_from": datetime, "valid_to": datetime, "active": boolean }` | Created coupon object                     | `IsAuthenticated`          |


## Example Request & Response

**Example GET Request for `/products/`**

Request:
GET /api/products/


Response:
```json
[
  {
    "id": 1,
    "name": "Product Name",
    "description": "Product description here",
    "price": 25.99,
    "stock": 100,
    "category": 2,
    "image": "/media/products/product_image.jpg",
    "created_at": "2025-03-08T14:30:00Z",
    "updated_at": "2025-03-08T14:30:00Z"
  }
]
