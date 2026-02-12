# 小游戏开发

## 1.javaScript

### 1.1.es6新增语法

#### 1.1.1.let和var

- let只在代码块内有效

```javascript
<script>
    for (var a = 0; a < 10; a++) {
    }
    console.log(a);
    // a = 10
    for (let b = 0; b < 10; b++) {
    }
    console.log(b);
    // b is not defined
</script>
```

- var可以重复声明，let不能重复声明

```javascript
<script>
    var a = 1;
    var a = 2; // 不会报错

    let b = 3;
    let b = 4; // 报错
</script>
```

- let不存在变量提升，var存在变量提升

```javascript
<script>
    console.log(a); // undefined
    var a = 1;

    console.log(b); // 报错
    let b = 2;
</script>
```

#### 1.1.2.const

- const声明一个只读的常量。一旦声明，常量的值就不能改变。

```javascript
<script>
    const PI = 3.1415926;
    PI = 3; // 报错
</script>
```

- const声明的变量不能改变，但是如果是一个对象，对象的属性是可以改变的。

```javascript
<script>
    const obj = {
        name: '张三',
        age: 18
    }
    obj.name = '李四'; // 不会报错
    obj = {}; // 报错
</script>
```

#### 1.1.3.Symbol

- Symbol是ES6引入的一种新的原始数据类型，表示独一无二的值。它是通过Symbol函数生成的。

```javascript
<script>
    let s1 = Symbol();
    let s2 = Symbol();
    console.log(s1 === s2); // false
</script>
```

- 使用Symbol作为对象属性名，可以保证不会出现重名属性。且Symbol属性名不能被枚举。有部分专门针对Symbol的内置方法，比如Object.getOwnPropertySymbols()，Reflect.ownKeys()等。

```javascript
<script>
    let s1 = Symbol('name');
    let s2 = Symbol('name');
    let obj = {
        [s1]: '张三',
        [s2]: '李四'
    }
    console.log(obj[s1]); // 张三
    console.log(obj[s2]); // 李四
    let obj = {
        [Symbol('name')]: '张三',
        age: 18, 
        title: 'Engineer'
    }

    console.log(Object.keys(obj)); //Symbol无法取到，是私有属性
    console.log(Object.getOwnPropertySymbols(obj)); //Symbol可以取到
    console.log(Reflect.ownKeys(obj)); //Symbol可以取到
</script>
```

#### 1.1.4. 解构赋值

- 数组解构赋值

```javascript
<script>
    let [a, ...b] = [1, 2, 3, 4]; // ...b表示剩余的元素
    console.log(b); // [2, 3, 4]
    let [a, b, c, d, e] = 'hello'; //可遍历对象都可以使用解构赋值
    console.log(a); // h
</script>
```

- 对象解构赋值

```javascript
<script>
    let {name, age} = {name: '张三', age: 18};
    let obj = {p : ['张三', {'age': 18}]};
    let {p: [x, {age}]} = obj;
    console.log(x); // 张三
    console.log(age); // 18
    let {a = 10, b = 5} = {a: 3}; // 解构默认值
    console.log(b); // 5
</script>
```

#### 1.1.5. 箭头函数

- 自执行函数

```javascript
<script>
    //自执行函数
    (function (n1, n2) {
        console.log(n1 + n2);
    }) (10, 100);

    (function (n1, n2) {
        console.log(n1 + n2);
    } (10, 110));
</script>
```

- 箭头函数

```javascript
<script>
    // 箭头函数
    let f = (a, b) => a + b;
    console.log(f(10, 20));

    let x = (a, b) => {
        let result = a + b;
        return result;
    }
    console.log(f(10, 30));
</script>
```

- 箭头函数中的this
  
  - 普通函数的this指向调用者，没有调用者指向window
  - 箭头函数的this指向定义时所在的对象，而不是调用时所在的对象
  - 箭头函数中的this，首先从父级作用域中查找，如果父级还是箭头函数，再往上找，直到找到this的指向
  
```javascript
<script>
    //this
    var str = "window"

    const obj = {
        str: "obj",
        nativeFn: function() {
            console.log(this.str, "this");
            return function() {
                console.log("native", this.str);
            }
        }, 
        arrowFn: function() {
            console.log(this.str, "this");
            return () => {
                console.log("arrow", this.str);
            }
        }
    }

    const obj2 = {
        str: "obj2"
    }

    var nativeFn = obj.nativeFn();
    var arrowFn = obj.arrowFn();

    nativeFn(); // window native，没有调用者默认指向window
    arrowFn(); // obj arrow，指向定义时的对象

    nativeFn.call(obj2); // obj2 native，调用者指向obj2
    arrowFn.call(obj2); // obj arrow，指向定义时的对象
</script>
```

### 1.2. Set和Array

- Set转Array

```javascript
<script>
    // Set Array
    let mySet = new Set(["value1", "value2", "value3"]);
    let myArray = [...mySet]; // 展开运算符

    console.log(mySet);
    console.log(myArray);
</script>
```

- Set可做数组去重、交集、并集、差集

```javascript
<script>
    // Set
    let mySet = new Set([1, 2, 3, 4, 5, 5, 5, 5]);
    console.log(...mySet); // 1 2 3 4 5

    let a = new Set([1, 2, 3]);
    let b = new Set([3, 4, 5]);
    let union = new Set([...a, ...b]); // 并集
    console.log(union); // Set { 1, 2, 3, 4, 5 }

    let intersect = new Set([...a].filter(x => b.has(x))); // 交集
    console.log(intersect); // Set { 3 }
</script>
```

### 1.3. 面向对象

#### 1.3.1. 函数嵌套实现面向对象

```javascript
<script>
    // 函数嵌套实现面向对象
    function Person(name, age) {
        let obj = {};
        obj.name = name;
        obj.age = age;
        obj.sayName = function() {
            console.log(this.name);
        }
        return obj; // 返回对象
    }

    let p1 = Person("Tom", 18);
    p1.sayName();
</script>
```


  









