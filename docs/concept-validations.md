# Concept Validations

## Property Bindings

__Expectation__

```python
A.width.bind(B.width)
A.width.bind(B.width + 10)
A.width.bind(B.width or C.width)
```

__Base Implementation__

`B.width` returns a special instance of class Property:

```python
class Property:
    qid: str  # qobject id
    name: str  # property name
    bound: list[tuple[Property, expression]]

    def bind(self, x):
        pass
```

`Property.def:bind.param:x` is a dynamic type. Generally we can mark it as the
following types:

- `Property`: for example, `A.width.bind(B.width)`.
- `SimpleExpression`: for example, `A.width.bind(B.width + 10)`. The simple
  expression can be equally translated to JavaScript code, which means we can
  use it directly in QML. That is very necessary to improve GUI performance and
  in most cases it is widely used.
- `ComplicatedExpression`: for example, `A.width.bind(B.width or C.width)`. The
  complicated expression is hard to translate it to JavaScript code with minimum
  effort, so we'll try to create a inline function to deliver it to QML side.
