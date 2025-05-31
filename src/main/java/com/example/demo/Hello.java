package com.example.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class Hello {

    @GetMapping("/api/hello")
    public String hello() {
        return "Hello, World, How are you! doing";
    }
}
// This is a simple Spring Boot application that defines a REST controller.
// The controller has a single endpoint `/api/hello` that returns a greeting message.
// To run this application, you would typically have a main class annotated with `@SpringBootApplication`
// that starts the Spring Boot application, similar to the `DemoApplication` class shown in the comment.
/*
To run this Spring Boot application for testing, you need a main class with the @SpringBootApplication annotation.
Create a file named DemoApplication.java in the same package (com.example.demo):

package com.example.demo;


@SpringBootApplication
public class DemoApplication {
    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
}

Then, build and run the application using Maven or Gradle:
- With Maven: mvn spring-boot:run
- With Gradle: ./gradlew bootRun

Once running, access http://localhost:8080/api/hello in your browser or with curl to test the endpoint.
*/