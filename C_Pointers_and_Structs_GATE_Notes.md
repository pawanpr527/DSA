
# C Pointers, Structs & Function Pointers — GATE Notes

## 1. Pointer Types and Their Purpose

### `int *`
- Used to access integer values.
- Pointer arithmetic moves in units of `sizeof(int)`.
```c
int x = 10;
int *p = &x;
printf("%d", *p);
```

### `char *`
- Used for **byte-wise memory access**.
- `sizeof(char) == 1` (guaranteed).
- Used for offset calculations inside memory blocks.
```c
char *cp = (char *)&x;
```

### `void *`
- Generic pointer to hold any address.
- Cannot be dereferenced or used for arithmetic directly.
- Must be cast before use.
```c
void *vp = &x;
```

---

## 2. Struct Memory Layout

```c
typedef struct {
    int a;
    int b;
    int (*fptr)(int,int);
} Node;
```

### Typical 64-bit Layout
```
Offset  Member
0       a (4 bytes)
4       b (4 bytes)
8       fptr (8 bytes)
```

- Struct members are stored **contiguously**
- Padding may be added by compiler for alignment

---

## 3. Address vs Value (CRITICAL)

| Expression | Meaning |
|----------|--------|
| `&n1` | Address of struct |
| `&n1.b` | Address of member |
| `n1.b` | Value of member |
| `n1.fptr` | Address of function |
| `&n1.fptr` | Address where function pointer is stored |

---

## 4. Accessing Struct Members Using Pointers

### Best Practice
```c
int *pb = &n1.b;
printf("%d", *pb);
```

### Manual Offset (without offsetof)
```c
int *pb = (int *)((char *)&n1 + sizeof(int));
printf("%d", *pb);
```

⚠️ Works only if no padding before `b`.

---

## 5. Why `char *` for Memory Arithmetic

Pointer arithmetic rule:
```
ptr + 1 → advances sizeof(type) bytes
```

| Pointer Type | Movement |
|-------------|----------|
| `char *` | 1 byte |
| `int *` | 4 bytes |
| `Node *` | sizeof(Node) |

Hence:
```c
(char *)&n1 + 4   // move 4 bytes inside struct
```

---

## 6. Function Pointers (GATE Favorite)

```c
int add(int a, int b) { return a + b; }

int (*fp)(int,int) = add;
```

### Valid Calls
```c
fp(2,3);        // VALID
(*fp)(2,3);     // VALID
```

### Invalid
```c
fp(2);          // wrong args
fp = fp(2,3);   // int → function pointer
add = fp;       // function not assignable
```

---

## 7. Printing Addresses (EXAM RULE)

✅ Correct:
```c
printf("%p", (void *)&x);
```

❌ Wrong:
```c
printf("%d", &x);
printf("%x", &x);
```

---

## 8. Inside vs Outside Object (Very Important)

Given:
```c
char *p = (char *)&n1;
```

| Expression | Meaning |
|----------|--------|
| `p + 0` | Inside object |
| `p + sizeof(int)` | Inside object |
| `p + sizeof(Node)` | One-past-end (cannot dereference) |
| `p + sizeof(Node) + 1` | Outside → UB |

---

## 9. GATE TRAPS (Must Remember)

1. Value ≠ Address
2. `void *` arithmetic is illegal
3. Function pointers ≠ data pointers
4. `%p` + `(void *)` mandatory
5. `fp()` == `(*fp)()` in C
6. One-past-end address allowed, dereference not allowed

---

## 10. One-Line Rules for Exam

- Address → `void *`
- Offset math → `char *`
- Value access → real type (`int *`, `struct *`)
- Never guess padding
- If confused → use `&member`

---

## 11. Common GATE MCQ Patterns

- Identify valid pointer arithmetic
- Detect undefined behavior
- Function pointer invocation
- Struct padding & alignment
- Printing addresses

---
