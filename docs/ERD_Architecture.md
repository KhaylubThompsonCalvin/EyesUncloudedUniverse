# EyesUnclouded.ai – Entity Relationship Diagram (ERD)

## Overview
This document provides a comprehensive breakdown of the EyesUncloudedUniverse data architecture. The ERD models the symbolic, interactive solar system that powers both the EyesUnclouded.ai and its gateway (Khaylub.com). It represents users, celestial interactions, virtue-emotion mechanics, mentor insights, and the unlocking system for gamified learning and legacy transmission.

---

## 1. User Model

The `users` table is the foundation of identity and progression in the EyesUnclouded system. It contains fields for Role Type (Seeker, Strategist, etc.), hidden Class (revealed through behavior), and Perception Score. Each user has a legacy key for unlocking descendant-only content.

---

## 2. Celestial System

- `celestial_bodies` models all symbolic objects: planets, moons, and the sun.
- `clickables` are interactive objects on each celestial body (e.g., projects, gateways, hidden trials).
- `navigation_links` describe movement paths between celestial locations or to external systems.

---

## 3. Unlock System

- `user_unlocks` tracks what content a user has accessed.
- `points_log` records how and when perception or virtue points were earned.
- `auth_gate` enforces access control (e.g., email verification, legacy token).

---

## 4. Virtue + Emotion Engine

- `virtues` and `expressions` define emotional and moral constructs.
- `virtue_expression_link` maps facial/emotional triggers to virtues.
- `user_notes` allow users to journal reflections.
- `sources` and `source_virtue_link` relate real-world insights to game logic.

---

## 5. Mentor System

- `mentor_lessons` delivers narrated insights tied to Role Type.
- Lessons are triggered by behavior, emotion logs, or symbolic events.

---

## 6. Perception Trials & Class Reveal

- `chapters` define symbolic moments like “Trial of the Chronopaths”.
- `perception_entries` log how a user emotionally and philosophically responded to trials.
- These feed into Class reveal logic (e.g., King of the Mole Order).

---

## Visual Assets

- The ERD file is located at: `diagrams/EyesUncloudedUniverse_ERD.dbml`
- Upload to [dbdiagram.io](https://dbdiagram.io/) for visualization

---

## Purpose & Future Use

This ERD ensures that all symbolic, emotional, and narrative components of EyesUnclouded.ai are structurally sound. It prepares the platform for:
- AI behavior modeling
- Secure legacy gating
- Immersive storytelling
- Descendant-oriented inheritance triggers
