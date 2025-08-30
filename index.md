# kitchen_sink

Kitchen Sink Schema

This schema does not do anything useful. It exists to test all features of linkml.

This particular text field exists to demonstrate markdown within a text field:

Lists:

   * a
   * b
   * c

And links, e.g to [Person](Person.md)

URI: https://w3id.org/linkml/tests/kitchen_sink

Name: kitchen_sink



## Classes

| Class | Description |
| --- | --- |
| [Activity](Activity.md) | a provence-generating activity |
| [Address](Address.md) | None |
| [Agent](Agent.md) | a provence-generating agent |
| [Dataset](Dataset.md) | None |
| [Event](Event.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BirthEvent](BirthEvent.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EmploymentEvent](EmploymentEvent.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MarriageEvent](MarriageEvent.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MedicalEvent](MedicalEvent.md) | None |
| [HasAliases](HasAliases.md) | None |
| [Organization](Organization.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Company](Company.md) | None |
| [Person](Person.md) | None |
| [Place](Place.md) | None |
| [Relationship](Relationship.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FamilialRelationship](FamilialRelationship.md) | None |
| [WithLocation](WithLocation.md) | None |



## Slots

| Slot | Description |
| --- | --- |
| [acted_on_behalf_of](acted_on_behalf_of.md) |  |
| [activities](activities.md) |  |
| [activity_set](activity_set.md) |  |
| [addresses](addresses.md) |  |
| [age_in_years](age_in_years.md) |  |
| [agent_set](agent_set.md) |  |
| [aliases](aliases.md) |  |
| [ceo](ceo.md) |  |
| [city](city.md) |  |
| [companies](companies.md) |  |
| [description](description.md) |  |
| [employed_at](employed_at.md) |  |
| [ended_at_time](ended_at_time.md) |  |
| [has_birth_event](has_birth_event.md) |  |
| [has_employment_history](has_employment_history.md) |  |
| [has_familial_relationships](has_familial_relationships.md) |  |
| [has_marriage_history](has_marriage_history.md) |  |
| [has_medical_history](has_medical_history.md) |  |
| [id](id.md) |  |
| [in_location](in_location.md) |  |
| [is_current](is_current.md) |  |
| [married_to](married_to.md) |  |
| [name](name.md) |  |
| [persons](persons.md) |  |
| [related_to](related_to.md) |  |
| [started_at_time](started_at_time.md) |  |
| [street](street.md) |  |
| [type](type.md) |  |
| [used](used.md) |  |
| [was_associated_with](was_associated_with.md) |  |
| [was_generated_by](was_generated_by.md) |  |
| [was_informed_by](was_informed_by.md) |  |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [DiagnosisType](DiagnosisType.md) |  |
| [FamilialRelationshipType](FamilialRelationshipType.md) |  |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
| [SubsetA](SubsetA.md) | test subset A |
| [SubsetB](SubsetB.md) | test subset B |
