function findroom() {

    const day = document.getElementById("day").value;
    const period = document.getElementById("period").value;

    const basePath = window.location.pathname.startsWith("/emptyclassroomfinder")
        ? "/emptyclassroomfinder"
        : "";

    const now = new Date();

    const date = now.toISOString().split("T")[0];

    const today = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
    ][now.getDay()];


    // Use cache only for today's data
    if (day === today) {

        const cacheKey = `timetable-${date}-${period}`;

        const cachedData = localStorage.getItem(cacheKey);

        if (cachedData) {

            console.log(
                `Using cached data for ${day}, Period ${period}`
            );

            displayRooms(JSON.parse(cachedData));

            return;
        }
    }


    // IF Cache doesn't exist then use backend
    console.log(
        `Fetching ${day}, Period ${period} from server`
    );

    fetch(`${basePath}/find?day=${day}&period=${period}`)
        .then(response => {

            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }

            return response.json();
        })
        .then(rooms => {

            // Cache the result if it is today's data
            if (day === today) {

                const cacheKey = `timetable-${date}-${period}`;

                localStorage.setItem(
                    cacheKey,
                    JSON.stringify(rooms)
                );
            }

            displayRooms(rooms);
        })
        .catch(error => {
            console.error("Failed to find rooms:", error);
        });
}


function displayRooms(rooms) {

    const results = document.getElementById("results");

    results.innerHTML = "";

    rooms.forEach(room => {

        const roomElement = document.createElement("p");

        roomElement.textContent = room;

        results.appendChild(roomElement);
    });
}
