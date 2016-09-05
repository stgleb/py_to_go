go:
	go build -buildmode=c-shared -o bin/main.go.so main.go

c:
	g++ -shared main.c -fPIC -o bin/main.c.so

clean:
	rm bin/*.*
