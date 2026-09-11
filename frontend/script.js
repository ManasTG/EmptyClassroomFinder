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

        // Heading
        const heading = document.createElement("h2");
        heading.textContent = "Available Classrooms";
        results.appendChild(heading);

        const info = document.createElement("p");
        info.textContent = `${day} • Period ${period}`;
        info.className = "result-info";
        results.appendChild(info);


        // Table
        const table = document.createElement("table");
        table.className = "result-table";

        table.innerHTML = `
        <thead>
        <tr>
        <th>#</th>
        <th>Classroom</th>
        </tr>
        </thead>
        `;


        const tbody = document.createElement("tbody");

        rooms.forEach((room, index) => {

            const row = document.createElement("tr");

            const number = document.createElement("td");
            number.textContent = index + 1;

            const roomName = document.createElement("td");
            roomName.textContent = room;

            row.appendChild(number);
            row.appendChild(roomName);

            tbody.appendChild(row);
        });


        table.appendChild(tbody);
        results.appendChild(table);
    });
}
