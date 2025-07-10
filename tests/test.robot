*** Settings ***
Library    AvroSerializer

*** Variables ***
${SCHEMA_FILE}    example_schema.avsc
${JSON_MSG}       {"name": "Dario", "age": 18, "email": "dario@example.com"}

*** Test Cases ***
Serialize JSON To Avro
    Load Avro Schema From File    ${SCHEMA_FILE}
    ${hex}=    Serialize And Return Hex    ${JSON_MSG}
    Log    Serialized Avro Hex: ${hex}
