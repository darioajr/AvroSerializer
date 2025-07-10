import pytest
from robot_avro_serializer.avroserializer import AvroSerializer

@pytest.fixture
def sample_schema(tmp_path):
    schema = {
        "type": "record",
        "name": "User",
        "fields": [
            {"name": "name", "type": "string"},
            {"name": "age", "type": "int"}
        ]
    }
    return schema

@pytest.fixture
def sample_data():
    return {"name": "Alice", "age": 30}

def test_avro_serializer_roundtrip(sample_schema, sample_data):
    serializer = AvroSerializer(sample_schema)
    avro_bytes = serializer.serialize(sample_data)
    result = serializer.deserialize(avro_bytes)
    assert result == sample_data