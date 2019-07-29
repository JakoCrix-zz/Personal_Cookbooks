# 05-actionButton

library(shiny)

ui <- fluidPage(
  # Everytime we click the button, it prints into console
  actionButton(inputId = "clicks", 
    label = "Click me")
)

server <- function(input, output) {
  observeEvent(input$clicks, {
    print(as.numeric(input$clicks))
  })
}


shinyApp(ui = ui, server = server)