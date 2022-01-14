def tongSo(n):
    total = 0;
    while (n > 0):
        total += n % 10;
        n = int(n / 10);
    return total;
# hàm tính tổng
n = int(input("Nhap n = "));
print("Tổng các số của n ", n, "la: ",tongSo(n));
ten = input('Tên: ');
print(ten);
print("Tổng các kí tự của ten ", ten, "la: ", len(ten));