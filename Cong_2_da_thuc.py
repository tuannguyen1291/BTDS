class Node:
    def __init__(self, heso, luythua):
        self.heso = heso
        self.luythua = luythua
        self.next = None

class DaThuc:
    def __init__(self):
        self.head = None

    def them(self, heso, luythua):
        if heso == 0:
            return
        node = Node(heso, luythua)
        if self.head is None or luythua > self.head.luythua:
            node.next = self.head
            self.head = node
        else:
            current = self.head
            while current.next and luythua < current.next.luythua:
                current = current.next
            node.next = current.next
            current.next = node

    def cong(self, dathuc):
        result = DaThuc()
        current1 = self.head
        current2 = dathuc.head
        while current1 and current2:
            if current1.luythua > current2.luythua:
                result.them(current1.heso, current1.luythua)
                current1 = current1.next
            elif current1.luythua < current2.luythua:
                result.them(current2.heso, current2.luythua)
                current2 = current2.next
            else:
                heso = current1.heso + current2.heso
                result.them(heso, current1.luythua)
                current1 = current1.next
                current2 = current2.next
        while current1:
            result.them(current1.heso, current1.luythua)
            current1 = current1.next
        while current2:
            result.them(current2.heso, current2.luythua)
            current2 = current2.next
        return result

    def __str__(self):
        if not self.head:
            return "0"
        values = []
        current = self.head
        while current:
            if current.heso == 1:
                heso = ""
            elif current.heso == -1:
                heso = "-"
            else:
                heso = str(current.heso)
            if current.luythua == 0:
                values.append(heso)
            elif current.luythua == 1:
                values.append(heso + "x")
            else:
                values.append(heso + "x^" + str(current.luythua))
            current = current.next
        return " + ".join(values)

# Ví dụ minh họa
dathuc1 = DaThuc()
dathuc1.them(2, 3)
dathuc1.them(1, 2)
dathuc1.them(3, 0)
print("Da thuc 1: " + str(dathuc1))

dathuc2 = DaThuc()
dathuc2.them(-1, 2)
dathuc2.them(2, 1)
dathuc2.them(4, 0)
print("Da thuc 2: " + str(dathuc2))

dathuc_tong = dathuc1.cong
