# Receipt Processor Challenge

This project is a Flask-based receipt processing application that uses Docker for easy deployment. It utilizes Redis for storing receipt information and provides an API to process receipts and calculate points.

## Prerequisites

- [Docker](https://www.docker.com/get-started)

## Getting Started

1. **Clone the repository:**

    ```bash
    git clone https://github.com/justbee007/fetch-reward-processor-challenge.git
    cd fetch-reward-processor-challenge
    ```

2. **Build the Docker images:**

    ```bash
    docker-compose build
    ```

3. **Run the Docker containers:**

    ```bash
    docker-compose up -d
    ```

    This will start the Flask app and Redis container.

4. **Verify that the containers are running:**

    ```bash
    docker-compose ps
    ```

    You should see the `flask-app` and `redis` containers listed.

5. **Access the API:**

    Open a tool like Postman, and use the following URL to process a receipt as a POST request with JSON as the request body:

    ```bash
    http://127.0.0.1:6000/receipts/process
    ```

    Use the API to calculate points. Use a GET request to get the points with a specific receipt ID:

    ```bash
    http://127.0.0.1:6000/receipts/<receipt-id>/points
    ```

6. **Flexibility with Ports:**

    The default setup assumes that ports 6000 and 6379 are available on your machine. If these ports are unavailable or you prefer different ports, you can customize them in the `docker-compose.yml` file:

    - Open the `docker-compose.yml` file.
    - Locate the `ports` section under the `flask-app` service. Change the left side of the mapping (before the colon) to the desired host port:

        ```yaml
        ports:
          - "6000:5000"
        ```

    - Save the file and run `docker-compose up -d` again.

7. **Sample JSON and Expected Result:**

    Sample JSON for processing a receipt:

    ```json
    {
      "retailer": "Target",
      "purchaseDate": "2022-01-01",
      "purchaseTime": "13:01",
      "items": [
        {
          "shortDescription": "Mountain Dew 12PK",
          "price": "6.49"
        },{
          "shortDescription": "Emils Cheese Pizza",
          "price": "12.25"
        },{
          "shortDescription": "Knorr Creamy Chicken",
          "price": "1.26"
        },{
          "shortDescription": "Doritos Nacho Cheese",
          "price": "3.35"
        },{
          "shortDescription": "Klarbrunn 12-PK 12 FL OZ",
          "price": "12.00"
        }
      ],
      "total": "35.35"
    }
    ```

    Expected result: The above receipt should return points 28.

## API Documentation

### Process Receipt

- **Endpoint:** `POST /receipts/process`
- **Request:**
  - **Content-Type:** `application/json`
  - **Body:**
    - Use JSON Schema for validation. (Include the JSON Schema details here)
    - Example:
      ```json
      {
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [
          {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
          },
          // ... (other items)
        ],
        "total": "35.35"
      }
      ```
- **Response:**
  - **Content-Type:** `application/json`
  - Example:
    ```json
    {
      "receiptId": "abc123"
    }
    ```

### Get Points for Receipt

- **Endpoint:** `GET /receipts/<receipt-id>/points`
- **Request:**
  - **Parameters:**
    - `receipt-id`: The unique identifier for the processed receipt.
- **Response:**
  - **Content-Type:** `application/json`
  - Example:
    ```json
    {
      "points": 28
    }
    ```

## JSON Schema for Validation

This project uses JSON Schema Draft-07 for validating the input JSON when processing a receipt. JSON Schema provides a clear structure for the expected format of the data, ensuring consistency and reliability.

For more details on JSON Schema Draft-07, refer to the official documentation: [JSON Schema Draft-07](https://json-schema.org/draft-07/json-schema-release-notes)

## Redis for Persistence

Redis is used as a persistence layer to store receipt information. This ensures that receipt data is retained even if the application or containers are restarted. Redis offers fast and efficient data storage and retrieval.

## Cleanup

To stop and remove the containers:

```bash
docker-compose down
