# UVG_CC3105
Repo for MLOps Course (CC3105) at UVG

---
[![Python CD](https://github.com/prof-aro-uvg/UVG_CC3105/actions/workflows/python-publish-v2.yml/badge.svg)](https://github.com/prof-aro-uvg/UVG_CC3105/actions/workflows/python-publish-v2.yml)
---

## Estimated Costs and Usage

**Real usage scenario:**
- **Classes:** Tuesday + Friday, ~4 hours per week.
- **Additional configuration time:** ~6 hours per week during the first month (setup, testing, adjustments).
- **Infrastructure:** Fully provisioned and destroyed weekly (no runtime costs outside planned hours).

---

### Estimated cost — Month 1 (setup + classes)

| Resource | Cost per hour | Estimated hours | Approx. subtotal |
|----------------|----------------|----------------|------------------|
| Kali `c5.9xlarge` | ~$1.53 USD | 45 h | ~$69 USD |
| Bastion `t2.micro` | ~$0.0116 USD | 45 h | ~$0.52 USD |
| NAT Gateway | ~$0.045 USD | 45 h | ~$2.02 USD |
| EBS Disk `gp3` 80–100 GB | ~$0.08 USD/GB-month | - | ~$6.40 USD |
| Snapshots (optional) | ~$0.05 USD/GB-month | - | ~$3 USD |

**Total Month 1:** **~$81–82 USD**

---

### Estimated cost — following months (class only)

| Resource | Cost per hour | Estimated hours | Approx. subtotal |
|----------------|----------------|----------------|------------------|
| Kali `c5.9xlarge` | ~$1.53 USD | 17 h | ~$26 USD |
| Bastion `t2.micro` | ~$0.0116 USD | 17 h | ~$0.20 USD |
| NAT Gateway | ~$0.045 USD | 17 h | ~$0.77 USD |
| EBS Disk `gp3` 80–100 GB | ~$0.08 USD/GB-month | - | ~$6.40 USD |
| Snapshots (optional) | ~$0.05 USD/GB-month | - | ~$3 USD |

**Total Month 2+:** **~$36–37 USD/month**

---

**Notes**
- **Always destroy** the infrastructure after each session to keep costs under control.
- Snapshots are optional and only needed if you want persistent backups.
- The EBS disk cost applies even when the instance is stopped, unless `delete_on_termination` is set and the instance is destroyed.

---

**This projection helps plan the semester’s budget and justify cloud expenses easily.**
