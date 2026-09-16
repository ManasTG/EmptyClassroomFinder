async function cacheToday() {

    const weekday = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
    ];

    const d = new Date();

    const dayName = weekday[d.getDay()];

    // YYYY-MM-DD
    const date = d.toISOString().split("T")[0];

    const basePath = window.location.pathname.startsWith("/emptyclassroomfinder")
    ? "/emptyclassroomfinder"
    : "";

    console.log(`Caching ${dayName} data for ${date}`);

    // To remove old timetable cache
    for (let key in localStorage) {
        if (key.startsWith("timetable-")) {
            localStorage.removeItem(key);
        }
    }

    for (let period = 0; period < 9; period++) {
        try {
            const response = await fetch(
                `${basePath}/find?day=${dayName}&period=${period + 1}`
            );

            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }

            const data = await response.json();

            localStorage.setItem(
                `timetable-${date}-${period + 1}`,
                JSON.stringify(data)
            );

            console.log(`Cached Period ${period + 1}`);

        } catch (error) {
            console.error(
                `Failed to cache Period ${period + 1}:`,
                error
            );
        }
    }

    console.log("Today's cache complete.");
}

cacheToday();
