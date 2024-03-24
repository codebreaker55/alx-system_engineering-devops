this project is about creating Web infrastructure design by whiteboarding.
###its required to be able to explain some specifics about this infrastructure.

* 0. Simple web stack

###Simplified Web Stack Overview
##Overview
This setup is a basic web system hosting a site accessible at www.foobar.com, lacking firewalls and SSL certificates for security. The server’s resources—CPU, RAM, SSD—are shared among its components, like the database and app server.

###Key Components Explained
##Server: A piece of computer hardware or software that offers services to other computers, known as clients.

##Domain Name: Acts as an easy-to-remember address for a website, like www.foobar.com, instead of using a numeric IP address. The Domain Name System (DNS) links the domain name to the IP address.

##DNS Record for www: www.foobar.com is linked to an IP address through an A record, found by using tools like dig.

##Web Server: The technology that processes requests via HTTP/HTTPS and sends back either the requested webpage or an error.

##Application Server: Hosts and manages web applications and services for users and organizations, ensuring the delivery of content.

##Database: Organizes and stores data in a way that makes it easy to retrieve, manage, and update.

##Communication: The server and client communicate over the internet using the TCP/IP protocol suite.

###Infrastructure Challenges
##Single Points of Failure (SPOF): The setup has several vulnerabilities. For example, if the database fails, the entire site goes down.

##Maintenance Downtime: Performing maintenance on any part requires shutting it down, leading to site unavailability due to the single-server setup.

##Difficulty Scaling: Handling increased traffic is a challenge with this structure since all components reside on one server, which can quickly become overwhelmed.

###Distributed Web Infrastructure Summary
##Overview
This infrastructure is designed to manage web traffic more effectively by spreading the load between a main server and a replica server, with a load balancer directing traffic to optimize server use.
--------------------------------------------------------------------------------------------------------------------------------------

* 1. Distributed web infrastructure

###Key Details

##Load Balancing Algorithm: Utilizes HAProxy with a Round Robin algorithm, cycling through servers based on their assigned weights to evenly distribute processing time. This dynamic method allows for real-time adjustment of server weights.

##Load Balancer Setup: Implements an Active-Passive configuration through HAProxy, where not all nodes serve workloads simultaneously. This setup ensures one node is always on standby to take over if the active node fails, enhancing reliability but not maximizing throughput as an Active-Active setup would.

##Primary-Replica Database Configuration: Features a Primary server for read/write operations and a Replica server primarily for read operations to minimize read traffic to the Primary. Data synchronization occurs after each write operation in the Primary server.

##Application Node Differences: The Primary node handles all write operations required by the website, while the Replica node assists by managing read requests, lightening the load on the Primary node.

###Infrastructure Challenges
##Single Points of Failure (SPOF): Several vulnerabilities exist; for instance, if the Primary database server fails, the site can't process changes. The load balancer and the application server linked to the primary database also represent single points of failure.

##Security Concerns: The absence of SSL certificates means data isn't encrypted, posing a risk of interception. Additionally, the lack of firewalls means there's no mechanism to block potentially harmful or unauthorized IP addresses.

##Lack of Monitoring: Without a monitoring system, it's difficult to assess the health or status of each server, hindering proactive management and response to issues.

This infrastructure aims to balance efficiency with reliability by distributing loads between servers and using a load balancer to manage traffic. However, it also faces significant challenges related to security, resilience against failures, and the need for comprehensive monitoring to maintain optimal operation.
-------------------------------------------------------------------------------------------------------------------------------------------------

* 2-secured_and_monitored_web_infrastructure
###Secured and Monitored Web Infrastructure Overview
##Overview
This web infrastructure consists of three servers that are secured and monitored, facilitating encrypted traffic to enhance security and reliability.

###Key Components and Their Purposes
##Firewalls: Serve to protect the web servers from unauthorized access by filtering incoming traffic based on predetermined security rules. They act as a barrier between the internal network (web servers) and the external network (internet), blocking traffic that doesn't meet security criteria.

##SSL Certificate: Used to encrypt data in transit between the web servers and the external network. SSL certificates help prevent man-in-the-middle (MITM) attacks and data interception by ensuring that all transmitted information is encrypted, thus maintaining privacy, data integrity, and authentication.

##Monitoring Clients: Deployed to continuously monitor the performance and health of the servers. These tools analyze server operations, track overall health metrics, and notify administrators of potential issues, ensuring that any performance degradation or operational anomalies are promptly addressed.

###Identified Infrastructure Challenges
##SSL Termination at Load Balancer: If SSL encryption is terminated at the load balancer, it means that traffic between the load balancer and the web servers is unencrypted, potentially exposing data to interception within the internal network.

##Single MySQL Server: Relying on a single MySQL server poses scalability challenges and introduces a single point of failure. If this server goes down, it can disrupt the entire web service.

##Homogeneous Server Components: Having identical components on all servers can lead to resource contention (CPU, Memory, I/O, etc.), negatively affecting performance. This setup complicates troubleshooting and scaling since it's more difficult to isolate problems or allocate resources efficiently.

###Conclusion
While this infrastructure enhances security through the use of firewalls and SSL certificates and improves reliability through monitoring, it also faces challenges regarding data encryption continuity, scalability, and performance optimization. Addressing these issues involves implementing end-to-end encryption, considering a distributed database approach, and possibly segregating server roles to better manage resources and scaling.
-------------------------------------------------------------------------------------------------------------------------------------------------
* 3. Scale up

###Description
##This web infrastructure is a scaled up version of the infrastructure described here. In this version, all SPOFs have been removed and each of the major components (web server, application server, and database servers) have been moved to separate GNU/Linux servers. The SSL protection isn't terminated at the load-balancer and each server's network is protected with a firewall and they're also monitored.

###Specifics About This Infrastructure
##The addition of a firewall between each server.
This protects each server from unwanted and unauthorized users rather than protecting a single server.
Issues With This Infrastructure
High maintenance costs.
Moving each of the major components to its own server, means that more servers would have to be bought and the company's electricity bill would rise along with the introduction of new servers. Some of the company's funds would have to be used to buy the servers and pay for the electricity consumption needed to keep the servers (including the new and old ones) running.
