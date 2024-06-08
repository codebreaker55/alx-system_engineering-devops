# Postmortem Report

## Website Outage

<p align="center">
<img src="https://github.com/codebreaker55/alx-system_engineering-devops/blob/master/0x19-postmortem/website-down.jpg" width=100% height=100% />
</p>

### Postmortem: Website Outage on June 7, 2024

#### Issue Summary:
**Summary**
On June 7, 2024, our e-commerce platform experienced a significant outage, The outage was caused by a load balancer misconfiguration, leading to an uneven distribution of traffic and overloading certain servers.
**Duration:**  
The outage lasted for 2 hours, from 5:00 PM to 7:00 PM EET.

**Impact:**  
During this period, our e-commerce platform was either completely inaccessible or extremely slow for approximately 80% of our users. Customers experienced timeouts and errors when attempting to load product pages or complete transactions. This resulted in a significant drop in sales and numerous customer complaints.

**Root Cause:**  
A misconfiguration in the load balancer led to an uneven distribution of traffic, overwhelming certain servers while leaving others underutilized.

#### Timeline(all times pacific Time):
- **5:00 PM** - Issue detected by monitoring alert indicating high response times and increased error rates.
- **5:05 PM** - Incident response team notified and investigation commenced.
- **5:10 PM** - Initial assumption: database overload due to increased traffic; database team began analysis.
- **5:20 PM** - Further investigation revealed database performance was normal, shifting focus to application servers.
- **5:30 PM** - Discovered several application servers were running hot while others were idle.
- **5:40 PM** - Load balancer misconfiguration suspected; network team involved.
- **6:00 PM** - Load balancer configuration reviewed; found incorrect weight settings causing uneven traffic distribution.
- **6:10 PM** - Configuration adjusted to distribute traffic evenly across all servers.
- **6:30 PM** - Servers began to stabilize as traffic distribution normalized.
- **7:00 PM** - Monitoring confirmed service restored to normal operation.

#### Root Cause and Resolution:
**Root Cause:**
The load balancer was configured with incorrect weight settings, causing it to send the majority of traffic to a subset of application servers. This led to these servers becoming overwhelmed while others remained underutilized. The configuration error occurred during a recent update to the load balancer settings, which was intended to optimize traffic distribution but was not properly tested before deployment.

**Resolution:**
The resolution involved identifying the misconfiguration in the load balancer and adjusting the weight settings to ensure an even distribution of traffic across all available application servers. Once the correct settings were applied, the system gradually returned to normal as the overloaded servers recovered and traffic was balanced appropriately.

### Recovery:
After the load balancer configuration was corrected, our team monitored the system closely to ensure all servers returned to their normal performance levels. Customer service was informed of the resolution, and affected users were notified of the service restoration. We implemented temporary measures to handle any residual traffic spikes and conducted a thorough review to ensure all aspects of the system were functioning optimally.

#### Corrective and Preventative Measures:
**Improvements:**
1. **Testing Configuration Changes:** Implement a more rigorous testing protocol for load balancer and other critical infrastructure changes.
2. **Monitoring Enhancements:** Improve monitoring to detect uneven server load distributions more rapidly.
3. **Incident Response Training:** Conduct regular training for the incident response team to handle similar issues more efficiently.

By addressing these areas, we aim to prevent similar incidents in the future and improve our overall service reliability.
