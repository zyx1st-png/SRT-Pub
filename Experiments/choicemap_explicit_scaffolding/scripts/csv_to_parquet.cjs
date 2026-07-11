"use strict";

const fs = require("fs");
const readline = require("readline");
const parquet = require("parquetjs-lite");

function parseCsvLine(line) {
  const out = []; let field = ""; let quoted = false;
  for (let i = 0; i < line.length; i++) {
    const ch = line[i];
    if (ch === '"') {
      if (quoted && line[i + 1] === '"') { field += '"'; i++; }
      else quoted = !quoted;
    } else if (ch === "," && !quoted) { out.push(field); field = ""; }
    else field += ch;
  }
  out.push(field); return out;
}

const intNames = new Set(["seed","episode","step","world_seed","current_task_success","future_task_success",
  "joint_success","irreversible_failure","successful_rollback","probe_count",
  "node_expansions","active_node_expansions","planning_calls","active_planning_calls",
  "environment_interactions","failed_run","available_evidence","irreversibility_level",
  "reactivated_count","initial_regime_template","shifted_regime_template"]);
const boolNames = new Set(["selected","non_dominated","blocked","is_probe","is_commitment","wrong_commitment"]);
const doubleNames = new Set(["commitment_time","rfs_auc","final_rfs","wall_clock_seconds","posterior_entropy",
  "top_probability","expected_current_return","worst_case_current_return","estimated_information_gain",
  "estimated_resource_cost","estimated_local_option_loss"]);

async function convert(input, output) {
  const rl = readline.createInterface({input: fs.createReadStream(input), crlfDelay: Infinity});
  let headers = null; let writer = null;
  for await (const line of rl) {
    if (!headers) {
      headers = parseCsvLine(line);
      const spec = {};
      for (const h of headers) {
        if (boolNames.has(h)) spec[h] = {type: "BOOLEAN", optional: true};
        else if (intNames.has(h)) spec[h] = {type: "INT64", optional: true};
        else if (doubleNames.has(h)) spec[h] = {type: "DOUBLE", optional: true};
        else spec[h] = {type: "UTF8", optional: true};
      }
      writer = await parquet.ParquetWriter.openFile(new parquet.ParquetSchema(spec), output, {useDataPageV2: false});
      continue;
    }
    if (!line) continue;
    const values = parseCsvLine(line); const row = {};
    headers.forEach((h, i) => {
      const raw = values[i] ?? "";
      if (raw === "" || raw === "nan" || raw === "NaN") return;
      if (boolNames.has(h)) row[h] = raw === "True" || raw === "true" || raw === "1";
      else if (intNames.has(h)) row[h] = Number.parseInt(raw, 10);
      else if (doubleNames.has(h)) row[h] = Number.parseFloat(raw);
      else row[h] = raw;
    });
    await writer.appendRow(row);
  }
  if (!writer) throw new Error(`empty CSV without header: ${input}`);
  await writer.close();
}

if (process.argv.length !== 4) throw new Error("usage: node csv_to_parquet.cjs input.csv output.parquet");
convert(process.argv[2], process.argv[3]).catch(err => { console.error(err); process.exit(1); });
