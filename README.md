# DealNavigator

![DealNavigator Logo](path/to/logo.png)

DealNavigator is a web application that allows users to search for products on Amazon and Flipkart, and view detailed information about the products, including price, rating, and more. The application is built using Flask for the backend and vanilla JavaScript for the frontend.

## Features

- Search for products on Amazon and Flipkart
- View detailed product information including price, rating, and reviews
- Sort products by price, rating count, and average rating
- Responsive design for mobile and desktop

## Screenshots

![DealNavigator Screenshot](path/to/screenshot.png)

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/DealNavigator.git
    cd DealNavigator
    ```

2. Build and run the Docker container:

    ```sh
    docker-compose up --build
    ```

3. Open your browser and navigate to `http://localhost:5000`.

### Usage

1. Enter a product name in the search bar.
2. Click the "Search" button.
3. View the search results and sort them using the sort options.

### Project Structure

- [backend](http://_vscodecontentref_/2): Contains the backend code including the Flask app and scrapers.
- [frontend](http://_vscodecontentref_/3): Contains the frontend code including HTML, CSS, and JavaScript.
- [Dockerfile](http://_vscodecontentref_/4): Docker configuration for building the container.
- `docker-compose.yml`: Docker Compose configuration for running the application.

### API Endpoints

- `POST /search`: Accepts a JSON payload with a [query](http://_vscodecontentref_/5) field and returns search results.
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

For any inquiries, please contact [yourname@example.com](mailto:yourname@example.com).

---

DealNavigator - Your ultimate tool for finding the best deals online!