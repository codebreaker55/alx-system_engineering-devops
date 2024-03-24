
<<<<<<< HEAD
Project Overview
0. Simple Web Stack
Simplified Web Stack Overview
This setup is a basic web system hosting a site accessible at www.foobar.com, lacking firewalls and SSL certificates for security. The server’s resources—CPU, RAM, SSD—are shared among its components, like the database and app server.

Key Components Explained

- Server: A piece of computer hardware or software that offers services to other computers, known as clients.
- Domain Name: Acts as an easy-to-remember address for a website, like www.foobar.com, instead of using a numeric IP address.
- DNS Record for www: www.foobar.com is linked to an IP address through an A record, found by using tools like dig.
- Web Server: The technology that processes requests via HTTP/HTTPS and sends back either the requested webpage or an error.
- Application Server: Hosts and manages web applications and services for users and organizations, ensuring the delivery of content.
- Database: Organizes and stores data in a way that makes it easy to retrieve, manage, and update.
- Communication: The server and client communicate over the internet using the TCP/IP protocol suite.
Infrastructure Challenges

- Single Points of Failure (SPOF): The setup has several vulnerabilities. For example, if the database fails, the entire site goes down.
- Maintenance Downtime: Performing maintenance on any part requires shutting it down, leading to site unavailability due to the single-server setup.
- Difficulty Scaling: Handling increased traffic is a challenge with this structure since all components reside on one server, which can quickly become overwhelmed.
1. Distributed Web Infrastructure
Key Details

* Load Balancing Algorithm: Utilizes HAProxy with a Round Robin algorithm to evenly distribute processing time.
* Load Balancer Setup: Implements an Active-Passive configuration through HAProxy.
* Primary-Replica Database Configuration: Features a Primary server for read/write operations and a Replica server primarily for read operations.
* Application Node Differences: The Primary node handles all write operations required by the website, while the Replica node assists by managing read requests.
Infrastructure Challenges

* Single Points of Failure (SPOF): Several vulnerabilities exist, such as the Primary database server failure.
Security Concerns: The absence of SSL certificates and firewalls poses risks of data interception and unauthorized access.
* Lack of Monitoring: Without a monitoring system, it's difficult to assess the health or status of each server.
2. Secured and Monitored Web Infrastructure
Overview
- This web infrastructure consists of three servers that are secured and monitored, facilitating encrypted traffic to enhance security and reliability.

Key Components and Their Purposes

* Firewalls: Serve to protect the web servers from unauthorized access by filtering incoming traffic.
SSL Certificate: Used to encrypt data in transit between the web servers and the external network.
* Monitoring Clients: Deployed to continuously monitor the performance and health of the servers.
Identified Infrastructure Challenges

* SSL Termination at Load Balancer: Potential exposure of data to interception within the internal network.
* Single MySQL Server: Relying on a single MySQL server poses scalability challenges and introduces a single point of failure.
* Homogeneous Server Components: Resource contention and scalability issues due to identical components on all servers.
- Conclusion
While this infrastructure enhances security and reliability, it faces challenges regarding data encryption continuity, scalability, and performance optimization.

3. Scale Up
* Description
This web infrastructure is a scaled-up version of the infrastructure described previously, addressing single points of failure and incorporating individual servers for major components.

* Specifics About This Infrastructure
The addition of a firewall between each server protects each server from unwanted and unauthorized users.

* Issues With This Infrastructure
High maintenance costs associated with additional servers and increased electricity consumption
