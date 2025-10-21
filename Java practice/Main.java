class Animal{
	Animal(){
		System.out.println("Hello from Animal");
	}

	Animal(int a, String b){
		System.out.printf("First int %d %s", a, b);
	}

	Animal(String b, int a){
		System.out.printf("First String %d %s%n", a, b);
	}
}


class Dog extends Animal{
	private int a;

	Dog(int a, String b){
		super(a, b);
	}
	Dog(String b, int a){
		super(b, a);
	}
}


class Main{
	public static void main(String[] args){
		Dog dog = new Dog("Hello from Dog", 3);
		System.out.println(dog.getClass().toString());
	}
}