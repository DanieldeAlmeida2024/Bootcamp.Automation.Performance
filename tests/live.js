import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,
  duration: '5s',
  thresholds: {
    checks: ['rate>0.99'],
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<1500', 'p(99)<3000'],
    iterations: ['count>30'],
  },
};

export default function () {
  const url = (__ENV.BASE_URL || 'http://127.0.0.1:8080') + '/api/cars';
  const response = http.get(url, { timeout: '5s' });
  check(response, {
    'GET /api/cars: status 200': (r) => r.status === 200,
    'GET /api/cars: exatamente cinco carros': (r) =>
      r.status === 200 && r.json().length === 5,
  });
  sleep(0.2);
}
