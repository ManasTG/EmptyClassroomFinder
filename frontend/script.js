function findroom() {
    const day = document.getElementById("day").value;
    const period = document.getElementById("period").value;

    const basePath = window.location.pathname.startsWith("/emptyclassroomfinder")
    ? "/emptyclassroomfinder"
    : "";

    fetch(`${basePath}/find?day=${day}&period=${period}`)
    .then(response => response.json())
    .then(rooms => {

        const results = document.getElementById("results");

        results.innerHTML = "";

        rooms.forEach(room => {
            const roomElement = document.createElement("p");
            roomElement.textContent = room;

            results.appendChild(roomElement);
        });

    });

}
