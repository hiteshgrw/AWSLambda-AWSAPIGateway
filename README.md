# AWSLambda-AWSAPIGateway
Use AWS Lambda to perform CRUD operations on a database and connect the function with other service to make it visible like a webpage.
About Docker – 
Docker is a container management service. The keywords of Docker are developed, ship and run anywhere. The whole idea of Docker is for developers to easily develop applications, ship them into containers which can then be deployed anywhere. The initial release of Docker was in March 2013 and since then, it has become the buzzword for modern world development, especially in the face of Agile-based projects.
The Docker application is a server that runs on a system and is controlled by a command called docker. The docker can run instances of an image which is a complete operating system packed into a file. This running instance is known as a container, as in a container for an operating system. You can start and stop these containers are per demand. You can also completely delete containers and images from the docker system. To get started, you can build an image from a base operating system image, and configure it to your specifications. To ease the repeated building and configuration of images, Docker uses a build file known as the Dockerfile.
About AWS Lambda & AWS API Gateway – 
AWS Lambda is an event-driven, serverless computing platform provided by Amazon as a part of Amazon Web Services. It is a computing service that runs code in response to events and automatically manages the computing resources required by that code.
Amazon API Gateway is a managed service that allows developers to define the HTTP endpoints of a REST API or a WebSocket API and connect those endpoints with the corresponding backend business logic. It also handles authentication, access control, monitoring, and tracing of API requests. Many Serverless applications use Amazon API Gateway, which conveniently replaces the API servers with a managed serverless solution.
API Gateway sits between the backend services of your API and your API’s users, handling the HTTP requests to your API endpoints and routing them to the correct backends. It provides a set of tools that help you manage your API definitions and the mappings between endpoints and their respective backend services. It can also generate API references from your definitions and make them available to your users as API documentation. API Gateway integrates with many other AWS services like AWS Lambda, AWS SNS, AWS IAM, and Cognito Identity Pools. These integrations allow for fully managed authentication and authorization layers, as well as detailed metrics and tracing for API requests.

So, this was the application designed using AWS Lambda and API Gateways to perform CRUD operations on to the database.
Conclusion –
So, the application has been designed using AWS Lambda Functions and AWS API Gateway and docker containers running the database on it. This implementation shows the use of microservices implementation over the monolithic implementation and further gives the developer feasibility to think about code and it’s working and transferring all the responsibility of managing the servers to AWS which runs the code on their specialized containers which are high reliable, scalable and available. Hence, the developer can focus on coding and providing user needs as justified.


To follow all the steps refers to the documentation at - https://docs.google.com/document/d/16SUjttLvJvcgrBSIpBkNUg8YsKv8tuOiYaz8iIRPKfg/edit?usp=sharing
