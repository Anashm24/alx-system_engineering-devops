## Postmortem: Web Stack Outage on May 24, 2020

# Issue Summary:

Duration: May 24, 2020, 10:00 AM - 12:30 PM (UTC)
Impact: The web application experienced intermittent downtime and sluggish performance, particularly affecting dynamic links and APIs. Approximately 20% of users encountered disruptions during the outage.
Root Cause: A flaw in the router component of the custom PHP framework led to incorrect routing and processing of dynamic links and API requests, resulting in service degradation.
Timeline:

* 10:00 AM: Issue detected as users reported inability to access dynamic links and intermittent errors in API responses.
* 10:15 AM: Engineering team commenced investigation, focusing on server logs and router configuration.
* 10:30 AM: Initial assumption made that the issue was related to server misconfiguration or database connectivity problems. Database team engaged for assistance.
* 10:45 AM: Misleading path pursued as database queries and server configurations were found to be normal. Attention shifted to router component.
* 11:00 AM: Incident escalated to senior developers and system architects due to prolonged service disruption.
* 11:15 AM: Flaw identified in router component code, causing incorrect parsing and routing of dynamic links and API requests.
* 11:30 AM: Engineers implemented temporary workaround to manually route affected requests while investigating permanent fix.
* 12:00 PM: Permanent fix developed and deployed to production environment.
* 12:30 PM: Service fully restored after router fix applied across all servers.
Root Cause and Resolution:

Root Cause: A flaw in the custom PHP framework's router component resulted in incorrect parsing and routing of dynamic links and API requests, leading to service degradation.
Resolution: Engineers developed and deployed a permanent fix to the router component, ensuring accurate parsing and routing of dynamic links and API requests.
Corrective and Preventative Measures:

# Improvements:
Implement comprehensive unit and integration tests for router component to detect and prevent similar issues in the future.
Establish proactive monitoring for dynamic link and API request processing to quickly identify any anomalies.
Tasks:
Develop and implement unit and integration tests for router component by end of week.
Integrate proactive monitoring for dynamic link and API request processing into existing monitoring systems by end of month.
Conclusion:

The web stack outage on May 24, 2020, was caused by a flaw in the custom PHP framework's router component, resulting in intermittent downtime and sluggish performance for dynamic links and APIs. Through diligent investigation and swift action, the root cause was identified and a permanent fix was deployed, restoring service within two and a half hours. To prevent similar incidents in the future, comprehensive testing and proactive monitoring measures will be implemented to ensure the reliability and stability of the web application.
