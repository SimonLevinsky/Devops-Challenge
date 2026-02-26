Javapackage com.devops.app;

      import org.springframework.web.bind.annotation.GetMapping;
      import org.springframework.web.bind.annotation.RestController;

      @RestControllerpublic
      class HelloController { 
        @GetMapping("/")
          public String index() { 
                return "200 OK - Application is running!"; 
                }
        }