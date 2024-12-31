# DealNavigator

![DealNavigator Logo](/frontend/image/iconmonstr-chart-3-240.png)

DealNavigator is a web application that allows users to search for products on Amazon and Flipkart, and view detailed information about the products, including price, rating, and more. The application is built using Flask for the backend and vanilla JavaScript for the frontend.

## Features

- Search for products on Amazon and Flipkart
- View detailed product information including price, rating, and reviews
- Sort products by price, rating count, and average rating
- Responsive design for mobile and desktop

## Screenshots

![DealNavigator Screenshot](/frontend/image/image.png)

## Getting Started

### Prerequisites

- Docker

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/raushan2410/DealNavigator.git
    cd DealNavigator
    ```

2. Build and run the Docker container:

    ```sh
    docker build -t <image-name> .
    docker run --name dealNavigator -d -p 5002:5000 <image-name>
    ```

3. Open your browser and navigate to `http://localhost:5002`.

### Usage

1. Enter a product name in the search bar.
2. Click the "Search" button.
3. View the search results and sort them using the sort options.

### Project Structure

- [backend](/backend/): Contains the backend code including the Flask app and scrapers.
- [frontend](/frontend/): Contains the frontend code including HTML, CSS, and JavaScript.
- [Dockerfile](/Dockerfile): Docker configuration for building the container.

### API Endpoints

- `POST /search`: Accepts a JSON payload with a query field and returns search results.
- `GET /product_info`: Serves the product information file.

### Technologies Used

- Flask
- BeautifulSoup
- Requests
- Docker
- JavaScript
- HTML
- CSS

### Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

### License

This project is licensed under the MIT License. See the LICENSE file for details.

### Contact

For any inquiries, please contact [singhraushan2410@gmail.com](mailto:singhraushan2410@gmail.com).

---

DealNavigator - Your ultimate tool for finding the best deals online!
