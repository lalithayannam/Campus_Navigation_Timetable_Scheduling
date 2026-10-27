
const source = document.getElementById("source");
const destination = document.getElementById("destination");

async function apiRequest(url, options = {}) {
  const response = await fetch(url, options);

  const data = await response.json().catch(() => ({
    detail: `Invalid server response (HTTP ${response.status})`
  }));

  if (!response.ok) {
    throw new Error(
      typeof data.detail === "string"
        ? data.detail
        : JSON.stringify(data.detail || data)
    );
  }

  return data;
}

// 1. Load campus locations
async function loadCampus() {
  const result = document.getElementById("routeResult");

  try {
    const data = await apiRequest("/api/campus");

    source.replaceChildren();
    destination.replaceChildren();

    data.nodes.forEach(node => {
      source.add(new Option(node.name, node.name));
      destination.add(new Option(node.name, node.name));
    });

    if (destination.options.length > 1) {
      destination.selectedIndex = Math.min(
        3,
        destination.options.length - 1
      );
    }

    result.textContent = data.nodes.length
      ? `${data.nodes.length} campus locations loaded successfully.`
      : "No campus locations were returned by the API.";
  } catch (error) {
    result.textContent = `Could not load campus locations: ${error.message}`;
  }
}

// 2. Find a route
async function findRoute() {
  const result = document.getElementById("routeResult");

  if (!source.value || !destination.value) {
    result.textContent = "Please select a source and destination.";
    return;
  }

  if (source.value === destination.value) {
    result.textContent = "Please select two different locations.";
    return;
  }

  const params = new URLSearchParams({
    source: source.value,
    destination: destination.value,
    algorithm: document.getElementById("algorithm").value
  });

  try {
    const data = await apiRequest(`/api/route?${params}`);

    result.replaceChildren();

    const heading = document.createElement("h3");
    heading.textContent = data.algorithm.toUpperCase();
    result.append(heading);

    const details = [
      `Route: ${data.path.join(" → ")}`,
      `Distance: ${Number(data.distance).toFixed(2)} units`,
      `Nodes visited: ${data.visited}`,
      `Complexity: ${data.complexity}`
    ];

    details.forEach(detail => {
      const p = document.createElement("p");
      p.textContent = detail;
      result.append(p);
    });
  } catch (error) {
    result.textContent = `Route search failed: ${error.message}`;
  }
}

// 3. Generate timetable
async function generateSchedule() {
  const result = document.getElementById("scheduleResult");
  const algorithm =
    document.getElementById("scheduleAlgorithm").value;

  result.textContent = "Generating timetable...";

  try {
    const data = await apiRequest("/api/schedule/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ algorithm })
    });

    result.replaceChildren();

    const summary = document.createElement("p");
    summary.textContent =
      `Algorithm: ${data.algorithm} | Classes scheduled: ${data.assignments.length}`;
    result.append(summary);

    if (data.conflicts?.length) {
      const warning = document.createElement("p");
      warning.className = "error";
      warning.textContent = data.conflicts.join(", ");
      result.append(warning);
    }

    const table = document.createElement("table");
    const headers = [
      "Code", "Course", "Teacher", "Room", "Time"
    ];

    const headerRow = table.createTHead().insertRow();

    headers.forEach(label => {
      const th = document.createElement("th");
      th.textContent = label;
      headerRow.append(th);
    });

    const tbody = table.createTBody();

    data.assignments.forEach(item => {
      const row = tbody.insertRow();

      [
        item.course,
        item.course_name,
        item.teacher,
        item.room,
        item.slot
      ].forEach(value => {
        row.insertCell().textContent = value ?? "";
      });
    });

    result.append(table);
  } catch (error) {
    result.textContent = `Scheduling failed: ${error.message}`;
  }
}

// 4. Search campus buildings
async function searchBuildings() {
  const query = document.getElementById("search").value.trim();
  const results = document.getElementById("searchResults");

  results.replaceChildren();

  if (!query) return;

  try {
    const data = await apiRequest(
      `/api/search?q=${encodeURIComponent(query)}`
    );

    if (!Array.isArray(data)) {
      throw new Error("Unexpected search response format.");
    }

    data.forEach(name => {
      const li = document.createElement("li");
      li.textContent = name;
      results.append(li);
    });

    if (data.length === 0) {
      const li = document.createElement("li");
      li.textContent = "No matching buildings found.";
      results.append(li);
    }
  } catch (error) {
    const li = document.createElement("li");
    li.textContent = `Search failed: ${error.message}`;
    results.append(li);
  }
}

// Load locations when the page opens
loadCampus();