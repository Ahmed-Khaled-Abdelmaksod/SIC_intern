# Protocols Comparison: HTTP vs MQTT vs CoAP

This document provides a quick comparison between the three main IoT communication protocols: **HTTP, MQTT, and CoAP**.

---

## Comparison Table

| Feature            | HTTP                         | MQTT                          | CoAP                          |
|--------------------|------------------------------|-------------------------------|-------------------------------|
| Transport          | TCP                          | TCP (often over TLS)          | UDP                           |
| Message Size       | Large, text-based            | Very small, binary            | Very small, binary            |
| Overhead           | High (headers, verbose)      | Low                           | Very low                      |
| Communication Type | Request/Response             | Publish/Subscribe             | Request/Response (REST-like)  |
| Use Case           | Web apps, file transfer      | Sensor data, messaging        | Constrained devices, IoT      |
| QoS Support        | No                           | Yes (0,1,2 levels)            | Basic reliability (Confirmable/Non-confirmable) |

---

**Summary**  
- Use **HTTP** when working with web apps, REST APIs, or large data.  
- Use **MQTT** for continuous sensor data and lightweight publish/subscribe messaging.  
- Use **CoAP** for very constrained IoT devices and when low power + low overhead is needed.  
