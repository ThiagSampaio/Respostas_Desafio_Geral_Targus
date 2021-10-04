FROM golang:latest

COPY hello.go .

RUN go build hello.go

EXPOSE 8080

CMD ["./hello"]