map = new Map()
key = prompt("Enter Key")
while(key != null) {
    map.set(key,"true")
    document.writeln(Array.from(map.keys()).toString() + "<br>")
    key = prompt("Enter Key")
}