**Cryptographic Algorithms and protocols** can be grouped into four main areas:
- **Symmetric encryption:** Used for encryption of blocks or streams of data. Faster
- **Asymmetric encryption:** Used for encryption of small blocks of data. Digital Signatures. Slower
- **Data Integrity Algorithms:** Used to protect blocks of data, such as messages from alteration.
- **Authentication Protocols:** Use of cryptographic algorithms designed to authenticate the identity of entities.

> **CIA triad**
> - Confidentiality
> - Integrity
> - Availability
> - Authenticity
> - Accountability -> non-repudiation

### Security Attacks
1. Passive Attacks:
	- Nature of eavesdropping on
	- Monitoring of transmission
	- Traffic analysis
	- Prevention by ***encryption***
2. Active Attacks:
	- Modification of data stream
	- Prevention by ***Digital Signature, Hashing, firewall***
	- 4 categories:
| Category | Description |
| ---- | --- |
| Masquerade | One entity pretends to be another entity | 
| Replay | The attacker eavesdrops the messages. Resends the correctly encrypted message|
| Modification of messages | Capture message, Alter it and send back |
| DOS (Denial of Service) | Prevents the normal use of server |

## X.800
X.800 defines a **security service** as a service that is provided by a **protocol layer** of communicating open systems and that **ensures adequte security** of the systems or of data transfer.
Divides these services into five categories:
1. Authentication
	- Peer entity authentication
	- Data Origin authentication
2. Access Control
3. Data Confidentiality
4. Data Integrity
5. Nonrepudiation
6. Availablity Service

### Security Mechanisms
1. **Specific security mechanisms**
	Incorporated into the **appropriate protocol layer** in order to provide security.
	* Encipherment => *encryption
	* Digital Signature => *prove source / protect against forgery
	* Access Control
	* Data Integrity
	* Authentication Exchange => *ensure identity of an entity
	*  Traffic Padding => *insertion of bits  into gaps in a data stream to frustrate traffic analysis attempts
	* Routing Control
	* Notarization => *use of trusted third party to assure certain properties of data exchange
2. **Pervasive security mechanisms**
	Mechanism that are **not specific** to any particular OSI security service.
	* Trusted Functionality => Established by a secuirity policy
	* Secuity Label
	* Event Detection
	* Security Audit Trial
	* Security Recovery

#### Relationship between security services and mechanisms:
![alt relationship between security services and mechanisms](../assets/relationship-between-services-and-mechanisms.jpg)

### Fundamental Security Design Principles
* Economy of mechanism
* Fail-safe defaults
* Complete mediation
* Open design
* Seperation of privilege
* Least privilege
* Least common mechanism
* Psychological acceptability
* Isolation
* Encapsulation
* Modularity
* Layering
* Least astonishment

# TO BE CONTINUED...
