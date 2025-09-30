n = int(input('Nhập số lượng mặt hàng '))
a = {}
for i in range(n):
    tmh = ('Nhập tên mặt hàng ')
    a[tmh] = input('Mặt hàng')
    sl = ('Số lượng')
    a[sl] = input('Số lượng ')
    dg = ('Đơn giá ')
    a[dg] = input('Nhập đơn giá ')
print(a)
