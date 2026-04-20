---
title: "traffic_control_parameters.proto"
description: "Markdown extract for com.digitalasset.canton.protocol.v30 / community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/traffic_control_parameters.proto."
---

# `community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/traffic_control_parameters.proto`

## Navigation

- [Protocol markdown contents](/reference/protocol/latest/contents)
- [Original protobuf package page](/reference/protobuf/packages/com-digitalasset-canton-protocol-v30)
- Package set: `com.digitalasset.canton.protocol.v30` | [com.digitalasset.canton.protocol.v31](/reference/protobuf/packages/com-digitalasset-canton-protocol-v31) | [com.digitalasset.canton.participant.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-participant-protocol-v30) | [com.digitalasset.canton.synchronizer.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-synchronizer-protocol-v30)
- Source file: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/traffic_control_parameters.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/traffic_control_parameters.proto)

## Related sections in this package

- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/acs_commitments.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/acs-commitments)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/common)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common_stable.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/common-stable)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/confirmation_response.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/confirmation-response)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/mediator.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/mediator)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/merkle.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/merkle)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/ordering_request.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/ordering-request)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/participant-reassignment)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/participant-transaction)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/quorum.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/quorum)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/sequencing)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing_parameters.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/sequencing-parameters)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/signed_content.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/signed-content)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/storage.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/storage)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronization.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/synchronization)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronizer_parameters.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/synchronizer-parameters)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/topology)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/versioned_google_rpc_status.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/versioned-google-rpc-status)

## Types in this section

- [com.digitalasset.canton.protocol.v30.SetTrafficPurchasedMessage](#type-com-digitalasset-canton-protocol-v30-settrafficpurchasedmessage)
- [com.digitalasset.canton.protocol.v30.TrafficConsumed](#type-com-digitalasset-canton-protocol-v30-trafficconsumed)
- [com.digitalasset.canton.protocol.v30.TrafficControlParameters](#type-com-digitalasset-canton-protocol-v30-trafficcontrolparameters)
- [com.digitalasset.canton.protocol.v30.TrafficPurchased](#type-com-digitalasset-canton-protocol-v30-trafficpurchased)
- [com.digitalasset.canton.protocol.v30.TrafficReceipt](#type-com-digitalasset-canton-protocol-v30-trafficreceipt)
- [com.digitalasset.canton.protocol.v30.TrafficState](#type-com-digitalasset-canton-protocol-v30-trafficstate)

## Extracted reference

<a id="type-com-digitalasset-canton-protocol-v30-settrafficpurchasedmessage"></a>
**Message `com.digitalasset.canton.protocol.v30.SetTrafficPurchasedMessage`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/traffic_control_parameters.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/traffic_control_parameters.proto)
- Fields: 4

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| member | `string` | optional |  |
| serial | `uint32` | optional |  |
| total_traffic_purchased | `uint64` | optional |  |
| physical_synchronizer_id | `string` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-trafficconsumed"></a>
**Message `com.digitalasset.canton.protocol.v30.TrafficConsumed`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/traffic_control_parameters.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/traffic_control_parameters.proto)
- Fields: 5

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| member | `string` | optional |  |
| extra_traffic_consumed | `uint64` | optional |  |
| base_traffic_remainder | `uint64` | optional |  |
| last_consumed_cost | `uint64` | optional |  |
| sequencing_timestamp | `int64` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-trafficcontrolparameters"></a>
**Message `com.digitalasset.canton.protocol.v30.TrafficControlParameters`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/traffic_control_parameters.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/traffic_control_parameters.proto)
- Fields: 7

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| max_base_traffic_amount | `uint64` | optional |  |
| max_base_traffic_accumulation_duration | `google.protobuf.Duration` | optional |  |
| read_vs_write_scaling_factor | `uint32` | optional |  |
| set_balance_request_submission_window_size | `google.protobuf.Duration` | optional |  |
| enforce_rate_limiting | `bool` | optional |  |
| base_event_cost | `uint64` | optional |  |
| free_confirmation_responses | `bool` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-trafficpurchased"></a>
**Message `com.digitalasset.canton.protocol.v30.TrafficPurchased`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/traffic_control_parameters.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/traffic_control_parameters.proto)
- Fields: 4

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| member | `string` | optional |  |
| serial | `uint32` | optional |  |
| extra_traffic_purchased | `uint64` | optional |  |
| sequencing_timestamp | `int64` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-trafficreceipt"></a>
**Message `com.digitalasset.canton.protocol.v30.TrafficReceipt`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/traffic_control_parameters.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/traffic_control_parameters.proto)
- Fields: 3

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| consumed_cost | `uint64` | optional |  |
| extra_traffic_consumed | `uint64` | optional |  |
| base_traffic_remainder | `uint64` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-trafficstate"></a>
**Message `com.digitalasset.canton.protocol.v30.TrafficState`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/traffic_control_parameters.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/traffic_control_parameters.proto)
- Fields: 6

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| extra_traffic_purchased | `int64` | optional |  |
| extra_traffic_consumed | `int64` | optional |  |
| base_traffic_remainder | `int64` | optional |  |
| last_consumed_cost | `uint64` | optional |  |
| timestamp | `int64` | optional |  |
| serial | `uint32` | optional |  |
