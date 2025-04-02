def productos_medios(x0, x1, d, n):
    numeros = [x0, x1]
    for _ in range(n):
        y = numeros[-2] * numeros[-1]
        y_str = str(y).zfill(2 * d)
        centro = y_str[len(y_str)//2 - d//2 : len(y_str)//2 + d//2]
        numeros.append(int(centro))
    resultados = [x / (10**d) for x in numeros[2:]]
    return resultados

x0 = 5015
x1 = 5734
d = 4
n = 5

numeros_generados = productos_medios(x0, x1, d, n)

print("| n  | X_n  | R_n   |")
print("|----|------|------|")
for i, r in enumerate(numeros_generados, start=2):
    print(f"| {i}  | {int(r * 10**d):04} | {r:.4f} |")
