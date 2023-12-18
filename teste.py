def main(name: str, age: int) -> str:
  return f"Hello {name} | you are {age} age | teste"

result = main("Matheus", 20)

result_teste = result.split('|')

print(result_teste[2])
