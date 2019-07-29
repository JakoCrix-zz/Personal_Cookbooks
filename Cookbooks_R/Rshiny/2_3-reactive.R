# 03- reactive

library(shiny)

ui <- fluidPage(
  sliderInput(inputId = "num", 
              label = "Choose a number", 
              value = 25, min = 1, max = 100),
  plotOutput("hist"),
  verbatimTextOutput("stats")
)

server <- function(input, output) {
  data=reactive({                # the reactive expression reacts first when there is changes
    rnorm(input$num)
  })
  output$hist <- renderPlot({
    hist(rnorm(data()))          # Note that the object needs to be called as a function
  })
  output$stats <- renderPrint({
    summary(rnorm(data()))       # Output 2
  })
}

shinyApp(ui = ui, server = server)