import http from 'k6/http';
import {check, sleep} from 'k6';
import { htmlReport } from "https://raw.githubusercontent.com/benc-uk/k6-reporter/main/dist/bundle.js";

export const options = {
    vus: 10,
    duration: '5s',
}

export default function(){
    const url = 'http://localhost:8080/api/cars';
    const response = http.get(url);
    const cars = response.json();
    check(response, {
        'status is 200': (r) => r.status === 200,
        'constains exactly 5 cars': () => cars.length === 5
    });

}

export function handleSummary(data) {
    return {
      "./report/report-customizado.html": htmlReport(data),
    };
  }