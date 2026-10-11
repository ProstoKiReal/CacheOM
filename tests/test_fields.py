import pytest

from cache_om import CacheModel, IntegerField, StringField


@pytest.mark.skip(reason="Not implemented")
def test_string_field_accepts_string_values() -> None:
    class StringValue(CacheModel):
        key_prefix = "test:string-field"
        value = StringField()

    instance = StringValue(value="hello")

    assert instance.value == "hello"


@pytest.mark.skip(reason="Not implemented")
def test_string_field_rejects_non_string_values() -> None:
    class StringValue(CacheModel):
        key_prefix = "test:string-field"
        value = StringField()

    with pytest.raises(TypeError):
        StringValue(value=123)


@pytest.mark.skip(reason="Not implemented")
def test_integer_field_accepts_integer_values() -> None:
    class IntegerValue(CacheModel):
        key_prefix = "test:integer-field"
        value = IntegerField()

    instance = IntegerValue(value=123)

    assert instance.value == 123


@pytest.mark.parametrize("value", ["123", 1.5, True])
@pytest.mark.skip(reason="Not implemented")
def test_integer_field_rejects_non_integer_values(value: object) -> None:
    class IntegerValue(CacheModel):
        key_prefix = "test:integer-field"
        value = IntegerField()

    with pytest.raises(TypeError):
        IntegerValue(value=value)
