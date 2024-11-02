class Product {

    name;
    price;
    constructor(name, price) {
        this.name = name
        this.price = price
        if (this.constructor == Product) {
            throw new Error("Abstract classes cannot be instantiated")
        }
    }

    getDescription() {
        throw new Error("Method 'getDescription()' must be implemented")
    }

    getPrice() {
        throw new Error("Method 'getPrice()' must be implemented")
    }
}


class Electronics extends Product {
    warranty_years;
    constructor(name, price, warranty_years) {
        super(name,price)
        this.warranty_years = warranty_years
    }

    getPrice() {
        return this.price
    }

    getDescription() {
        return `${this.constructor.name}: ${this.name}, Warranty: ${this.warranty_years} years`
    }
}


class Book extends Product {

    author;

    constructor(title, price, author) {
        super(title,price)
        this.author = author
    }

    getPrice() {
        return this.price
    }

    getDescription() {
        return `${this.constructor.name}: ${this.name}, Author: ${this.author}`
    }
}

class Clothing extends Product {
    size;

    constructor(name, price, size) {
        super(name,price)
        this.size = size
    }

    getPrice() {
        return this.price
    }

    getDescription() {
        return `${this.constructor.name}: ${this.name}, Size: ${this.size}`
    }
}


class ProductFactory {
    constructor() {
        if (this.constructor == ProductFactory) {
            throw new Error('Abstract classes cannot be instantiated')
        }
    }

    create() {
        throw new Error("Method 'create()' must be implemented")
    }
}

class ElectronicFactory extends ProductFactory {
    create() {
        return new Electronics("Smatphone",699.99,2)
    }
}

class BookFactory extends ProductFactory {
    create() {
        return new Book("The Lord of the Rings", 59.99, "J.R.R. Tolkien")
    }
}

class ClothingFactory extends ProductFactory {
    create() {
        return new Clothing("T-shirt", 19.99, 'L')
    }
}


function client_order(factory) {
    product = factory.create()
    console.log(`Client: I'm currently creating a ${product.constructor.name}`)
    console.log(`Description - ${product.getDescription()}\n`)
}


function main() {
    console.log("App: Launching with Electronics Factory")
    client_order(new ElectronicFactory())

    console.log("App: Launching with Book Factory")
    client_order(new BookFactory())

    console.log("App: Launching with Clothing Factory")
    client_order(new ClothingFactory())
}

main()