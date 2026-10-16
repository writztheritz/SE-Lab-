# Lab 3: Component Modelling and Architectural Pattern Selection

## Objective
Evaluate architectural styles, select a suitable architecture for the assigned system, and create a UML Component Diagram showing components, interfaces, and dependencies.

## Assigned System
Restaurant Table Booking & Pre-Ordering App

## Tools
A UML modelling tool such as draw.io, Lucidchart, or StarUML.

## Architectural Styles Considered
- Layered Architecture
- Microservices Architecture
- Client-Server Architecture

## Selected Architecture
Three-tier Layered Architecture:

1. Presentation Layer — customer-facing web or mobile interface.
2. Business Layer — reservation, menu, order, and payment-related logic.
3. Data Layer — persistent storage and data access.

## Architectural Justification

### Separation of Concerns
Separate presentation, business logic, and data access so that changes to one area have less impact on the others.

### Transaction Coordination
Keep reservation and ordering operations closely coordinated, with the aim of preventing inconsistent outcomes such as orders without confirmed seating or duplicate table reservations.

### Security Considerations
Mediate access to sensitive data through the business layer, where validation and access-control checks can be applied.

### Performance Considerations
Co-located business components can communicate through in-process calls, reducing network communication overhead compared with separately deployed services.

## Component Diagram Requirements
The lab requires:
- At least five components
- At least four interfaces between components
- Appropriate UML component notation
- Provided and required interfaces using ball-and-socket notation where applicable
- Clearly labelled interactions and dependencies

## Lab Workflow
1. Review the assigned scenario.
2. Identify functional and non-functional requirements.
3. Compare the architectural styles.
4. Select an architecture and identify the main components.
5. Draw the UML Component Diagram.
6. Document the architectural choice, two supporting reasons, one security advantage, and one performance benefit.
7. Review and export the diagram and justification.

## Submission Contents
- UML Component Diagram
- Selected architectural style
- Two scenario-specific reasons for the selection
- Security advantage
- Performance benefit

## Lab Report
[View the Lab 3 submission](./SE_Lab_3.pdf)

## Learning Outcomes
- Compare architectural patterns against system requirements.
- Identify components, interfaces, and dependencies.
- Model a system using a UML Component Diagram.
- Explain architectural decisions and their security and performance implications.

## Student Details
- Name: Rithish PM
- SRN: PES2UG24CS405
