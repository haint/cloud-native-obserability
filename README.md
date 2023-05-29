**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

*TODO:* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation

### Pods in all Namespaces
<img src="https://raw.githubusercontent.com/haint/cloud-native-obserability/main/answer_img/todo1.1.png">

### Services in all Namespaces
<img src="https://raw.githubusercontent.com/haint/cloud-native-obserability/main/answer_img/todo1.2.png">

### Pods and Services in Monitoring and Observability Namespaces
<img src="https://raw.githubusercontent.com/haint/cloud-native-obserability/main/answer_img/todo1.3.png">

## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.
<img src="https://raw.githubusercontent.com/haint/cloud-native-obserability/main/answer_img/todo2.1.png">

## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.
<img src="https://raw.githubusercontent.com/haint/cloud-native-obserability/main/answer_img/todo3.1.png">
<img src="https://raw.githubusercontent.com/haint/cloud-native-obserability/main/answer_img/todo3.2.png">

## Describe SLO/SLI
*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.
- To indicate SLO *monthly uptime*, we need SLI is the rate of the 20x or 30x (valid requests) responses of the website in a total incoming requests per month
- To indicate SLO *request response time 700ms*, we need SLI for a request response time is how long the request took to be served in actuality.

## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs.

1. The average 20x or 30x responses of the web application
2. It took an average of 700ms for incoming requests to be served
3. 1.5% of the total incoming requests had 50x responses
4. The average CPU usage of the web application
5. The login requests in the web application for a month took an average of 2 seconds to be served

## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.
<img src="https://raw.githubusercontent.com/haint/cloud-native-obserability/main/answer_img/todo6.1.png">

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here. Also provide a (screenshot) sample Python file containing a trace and span code used to perform Jaeger traces on the backend service.
<img src="https://raw.githubusercontent.com/haint/cloud-native-obserability/main/answer_img/todo7.1.png">
<img src="https://raw.githubusercontent.com/haint/cloud-native-obserability/main/answer_img/todo7.2.png">

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.
<img src="https://raw.githubusercontent.com/haint/cloud-native-obserability/main/answer_img/todo8.1.png">

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue also include a screenshot of the tracer span to demonstrate how we can user a tracer to locate errors easily.

TROUBLE TICKET

Name: Ethan Nguyen

Date: 24 May 2023

Subject: Backend Service get star shows "Internal Server Error" error 500.

Affected Area: star enpoint

Severity: High

Description: No implementation to get star


## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name four SLIs that you would use to measure the success of this SLO.

  # SLO
  1. 99.95% of uptime per month
  2. 99.9% of responses to our front-service will return 2xx, 3xx or 4xx HTTP code within 2000 ms.
  3. 99.99% of transaction requests will succeed over any calendar month.
  4. 99.9% of backend service requests will succeed on their first attempt.


  # SLI
  1. less than 10 error responses in the last 24 hours.
  2. average response time of < 2000ms per minute.
  3. 75% more successful responses than errors.
  4. 99% of our responses had the right data format.


## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create a list of 2-3 KPIs to accurately measure these metrics as well as a description of why those KPIs were chosen. We will make a dashboard for this, but first write them down here.

1. We got less than 10 error responses in the last 24 hours.
    + Successful requests per minute:  this KPI indicates how well is performed our system.
    + Error requests per minute: this KPI is an analogous of this SLI.
    + Uptime - this KPI indicates if errors are comming from downtime or not.
2. We got an average response time of < 2000ms in the las 24 hours.
    + Average response time:  this KPI is an analogous of this SLI.
    + Uptime - this KPI will help us to determine if response time is affected by downtime of a service.
3. We got 75% more successful responses than errors.
    + Successful requests per minute:  this KPI indicates the number of successful request.
    + Error requests per minute: this KPI indicates the number of error requests.
## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.

<img src="https://raw.githubusercontent.com/haint/cloud-native-obserability/main/answer_img/final_dashboard.png">
<img src="https://raw.githubusercontent.com/haint/cloud-native-obserability/main/answer_img/final_dashboard_2.png">